// Copyright (c) 2023, Jinal Balar and contributors
// For license information, please see license.txt

frappe.ui.form.on('Property Owner', {
	refresh: function(frm) {
		frm.set_query("property", function () {
			if (frm.doc.property) {
			  return {
				query: "property_app.property_app.doctype.property_owner.property_owner.ower_property",
				filters: {
				  owner: frm.doc.owner,
				},
			  };
			} 
		  });
	}
});
