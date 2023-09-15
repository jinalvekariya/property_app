import frappe
from frappe.utils import today, add_years

def update_lease_agreements():
    current_date = today()

    one_year_from_now = add_years(current_date, 1)

    lease_agreements_to_update = frappe.get_all(
        'Lease Agreement',
        filters={'lease_end_date': current_date},
        fields=['lease_name']
    )

    for lease in lease_agreements_to_update:
        try:
            frappe.db.set_value('Lease Agreement', lease.lease_name, 'lease_end_date', one_year_from_now)
            frappe.db.commit()
        except Exception as e:
            frappe.log_error(f"Error updating lease agreement {lease.lease_name}: {str(e)}")

