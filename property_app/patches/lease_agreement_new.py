import frappe
from frappe.utils import nowdate, add_days

def execute():
    today = nowdate()
    future_date = add_days(today, 30)

    lease_agreements = frappe.get_all(
        "Lease Agreement",
        filters={
            "status": "Active",
            "lease_end_date": ("<=", future_date),
        },
        fields=["lease_name"],
    )
    
    for agreement in lease_agreements:
        lease_doc = frappe.get_doc("Lease Agreement", agreement.lease_name)
        lease_doc.status = "Pending Renewal"
        lease_doc.save(ignore_permissions=True)

    frappe.db.commit()