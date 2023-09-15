import frappe
import string
import random

def corn():

    print("/n/n New Note Inserted /n/n")
    letters = string.ascii_letters
    payment_record = " ".join(random.choice(letters) for i in range(10))

    new_note = frappe.get_doc({"doctype": "Payment Record",
                               "title": payment_record
                               })
    new_note.insert()
    frappe.db.commit()