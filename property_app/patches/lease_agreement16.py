import frappe
from datetime import datetime, timedelta

def execute():
    today = datetime.now().date()
    threshold_date = today + timedelta(days=30)

    lease_agreements = frappe.get_list(
        "Lease Agreement",
        filters={"lease_end_date": ("<=", threshold_date)},
        fields=["lease_name", "lease_end_date"]
    )

    for lease_agreement in lease_agreements:
        doc = frappe.get_doc("Lease Agreement", lease_agreement.lease_name)
        remaining_days = (doc.lease_end_date - today).days
        doc.duration = remaining_days

        if remaining_days < 0:
            doc.status = "Terminated"
        elif remaining_days < 30:
            doc.status = "Pending Renewal"
        else:
            doc.status = "Active"

        doc.save()

