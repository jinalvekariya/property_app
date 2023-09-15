// Copyright (c) 2023, Jinal Balar and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Monthly Rent Collection Report"] = {
	"filters": [
		{
			"fieldname":"select_month",
			"label":"Select Month",
			"fieldtype":"Select",
			"options":["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
		},
		{
			"fieldname":"select_year",
			"label":"Select Year",
			"fieldtype":"Select",
			"options":[2022,2023]
	
		}
	]
};
