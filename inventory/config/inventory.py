from __future__ import unicode_literals
from frappe import _

def get_data():
	return [

		{
			"label": _("Report"),
			"items": [

				{
					"type": "report",
					"name": "Ending Stock",
					"is_query_report": True,
					"doctype": "Report Center"
				},
				{
					"type": "report",
					"name": "Stock Card",
					"is_query_report": True,
					"doctype": "Report Center"
				},
				{
					"type": "report",
					"name": "Stock Availables",
					"is_query_report": True,
					"doctype": "Report Center"
				},
			]
		},
	]
