# Copyright (c) 2013, molie and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.utils import cint, flt, cstr, fmt_money
from frappe import _

def execute(filters=None):
	if not filters: filters = {}

	columns = get_columns()
	data = get_list_item_product(filters)

	return columns, data

def get_columns():
	return [
		_("Item Code")+":Link/Item:150",
		_("Item Name") + ":Data:400",
		_("Warehouse") + ":Data:150",
		_("Qty") + ":Float:100",
		_("StockUOM") + ":Data:100",
	]

def get_list_item_product(filters):
	conditions = get_conditions(filters)
	return frappe.db.sql("""
	select
     	sle.`item_code`,
     	it.`item_name`,
     	sle.`warehouse`,
     	sum(IF(sle.voucher_type = 'Stock Reconciliation',sle.qty_after_transaction,sle.actual_qty)) as actualqty,
		sle.`stock_uom`
	FROM
     	`tabStock Ledger Entry` sle, `tabItem` it
    WHERE
     	sle.`item_code` = it.`name` AND
     	sle.`docstatus` = '1' %s
	GROUP BY
		sle.item_code,sle.warehouse
	HAVING
		((sum(IF(sle.voucher_type = 'Stock Reconciliation',sle.qty_after_transaction,sle.actual_qty)) > 0)
		or (sum(IF(sle.voucher_type = 'Stock Reconciliation',sle.qty_after_transaction,sle.actual_qty)) < 0))
	""" %conditions, as_list=1)

def get_conditions(filters):
	conditions = ""
	if filters.get("to_date"):
		#conditions += "and posting_date >= '%s'" % frappe.db.escape(filters["from_date"])
		conditions += "and sle.posting_date <= '%s'" % frappe.db.escape(filters["to_date"])

	if filters.get("item_code"):
		#conditions += "and posting_date >= '%s'" % frappe.db.escape(filters["from_date"])
		conditions += "and sle.item_code = '%s'" % frappe.db.escape(filters["item_code"])

	if filters.get("warehouse"):
		#conditions += "and posting_date >= '%s'" % frappe.db.escape(filters["from_date"])
		conditions += "and sle.warehouse = '%s'" % frappe.db.escape(filters["warehouse"])

	return conditions
