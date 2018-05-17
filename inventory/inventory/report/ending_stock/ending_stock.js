// Copyright (c) 2016, ridhosribumi and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Ending Stock"] = {
	// Copyright (c) 2016, Ridhosribumi and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Ending Stock"] = {
	"filters": [
		{
			"fieldname":"to_date",
			"label": __("To Date"),
			"fieldtype": "Date",
			"width": "80",
			"default": frappe.datetime.get_today()
		},
		{
			"fieldname": "item_code",
			"label": __("Item"),
			"fieldtype": "Link",
			"width": "80",
			"options": "Item"
		},
		{
			"fieldname": "warehouse",
			"label": __("Warehouse"),
			"fieldtype": "Link",
			"width": "80",
			"options": "Warehouse"
		},
	],

}
