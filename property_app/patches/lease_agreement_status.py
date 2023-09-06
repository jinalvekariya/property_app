import datetime
import frappe

def execute():

    expiration_threshold = datetime.date.today() + datetime.timedelta(days=30)

    leases_to_update = frappe.db.get_list("Lease Agreement", filters={"lease_end_date": ["<=", expiration_threshold], "status": "Active"})

    for lease in leases_to_update:
        lease_doc = frappe.db.get_doc("Lease Agreement", lease.name)

        lease_doc.status = "Expired"
        lease_doc.save()