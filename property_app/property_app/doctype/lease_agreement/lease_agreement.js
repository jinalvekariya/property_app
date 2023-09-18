// Copyright (c) 2023, Jinal Balar and contributors
// For license information, please see license.txt

frappe.ui.form.on('Lease Agreement', {
    property: function(frm) {
        if (frm.doc.property) {
            frappe.call({
                method: 'frappe.client.get',
                args: {
                    doctype: 'Property',
                    filters: { name: frm.doc.property }, 
                    fieldname: ['rent_amount', 'security_deposit']
                },
                callback: function(response) {
                    if (response.message) {
                        frm.doc.rent_amount = response.message.rent_amount;
                        frm.doc.security_deposit = response.message.security_deposit;
                        frm.refresh();
                    }
                }
            });
        }
    }
});
