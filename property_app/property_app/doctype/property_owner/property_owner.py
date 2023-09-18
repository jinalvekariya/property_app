# Copyright (c) 2023, Jinal Balar and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class PropertyOwner(Document):
	pass

@frappe.whitelist()
def ower_property(doctype, txt, searchfield, start, page_len, filters):
    if filters:
        query = """
                SELECT DISTINCT `tabProperty`.property_name as name
                FROM 
                `tabProperty`
                WHERE 
                 `tabProperty`.property_name = %(owner)s  AND
                 `tabProperty`.{key} LIKE %(txt)s
        """
        values = frappe.db.sql(query.format(
            key=searchfield
        ),
            {
            "owner": filters["owner"],
            'txt': "%{}%".format(txt),
            'start': start,
            'page_len': page_len
        })
        return values

