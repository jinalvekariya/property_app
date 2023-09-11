// Copyright (c) 2023, Jinal Balar and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Property Maintenance Report"] = {
	"filters": [
		{
            "fieldname": "status",
            "label": "Status",
            "fieldtype": "Select",
            "options": ["Open", "In Progress", "Closed"],
            "default": "Open",
        },
        {
            "fieldname": "assigned_to",
            "label": "Assigned To",
            "fieldtype": "Link",
            "options": "Maintenance Staff",
        },
	]
};
