# Copyright (c) 2023, tmf.one and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
import requests
import json

class RemoteSyncOptions(Document):
	def __init__(self, *args, **kwargs):
		super(RemoteSyncOptions, self).__init__(*args, **kwargs)

	def validate(self):
		url = f"{self.remote_instance}/api/method/frappe_dev.tmf_toolbox.utils.execute_db_query"
		query = """select * from `tabCompany`"""
		headers = {
        'Authorization': f"token {self.get_password(fieldname='authorization')}",
        'Content-Type': 'application/json'
        }
		payload = json.dumps({"query": query})
		try:
			response = requests.request("POST", url, headers=headers, data=payload)
		except:
			frappe.throw("Not a valid remote instance. Please check the URL.")
		if response.status_code != 200:
			frappe.throw("Authorization failed or not a valid remote instance")

