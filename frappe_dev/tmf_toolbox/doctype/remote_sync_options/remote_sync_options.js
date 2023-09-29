// Copyright (c) 2023, tmf.one and contributors
// For license information, please see license.txt

frappe.ui.form.on('Remote Sync Options', {
	refresh: function(frm) {
		frm.add_custom_button("Sync Now", () => {
			frappe.confirm('Are you sure you want to proceed? This will create a background job that copies data from the remote server to your local DB.',
			() => {
				frappe.call({
					method: 'frappe_dev.tmf_toolbox.utils.sync_with_remote_enqueue',
					args: {},
					callback: function(r) {
						if (!r.exc) {
							// code snippet
							frappe.msgprint("Background Job Created!");
						}
					}
				});
			}, () => {
				// action to perform if No is selected
			})
		});
	}
});