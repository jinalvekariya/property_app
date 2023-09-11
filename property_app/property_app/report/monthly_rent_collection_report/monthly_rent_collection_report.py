# Copyright (c) 2023, Jinal Balar and contributors
# For license information, please see license.txt

import frappe

def execute(filters=None):
    columns = get_columns()
    data = get_data(filters)
    
    return columns, data

def get_columns():
    return[
        "Property::200",
		"Tenant::200",
		"Rent Collected::200",
		"Payment Date::200"
  	]
    
def get_data(filters=None):
    data = []
    select_month = 0

    if filters and "select_month" in filters:
        months = {"January": 1, "February": 2, "March": 3, "April": 4, "May": 5, "June": 6, "July": 7, "August": 8, "September": 9, "October": 10, "November": 11, "December": 12}
        select_month = months.get(filters["select_month"], 0)

    property = frappe.db.get_all('Payment Record', fields=["property", "tenant", "rent_collected", "payment_date"])
    for tenant in property:
        date = tenant.payment_date
        if(filters.select_month and filters.select_year):
            if (date.month==select_month and date.year==int(filters.select_year)):
                row={
						"property":tenant.property,
						"tenant":tenant.tenant,
						"rent_collected":tenant.rent_collected,
						"payment_date":tenant.payment_date
					}
                data.append(row)
    return data   
