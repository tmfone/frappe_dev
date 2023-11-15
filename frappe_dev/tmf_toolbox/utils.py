import frappe

import requests
import json
import datetime

@frappe.whitelist(allow_guest=True)
def get_whitelisted_methods():
    whitelisted_functions = []
    for e in frappe.whitelisted:
        whitelisted_functions.append(f"{getattr(e, '__module__')}.{getattr(e, '__name__')}")
    for e in frappe.guest_methods:
        whitelisted_functions.append(f"{getattr(e, '__module__')}.{getattr(e, '__name__')}")
    return(whitelisted_functions)


@frappe.whitelist()
def sync_with_remote():
    user = frappe.session.user
    if user != "Administrator":
        return("Can only be executed by user 'Administrator'")
    # Known Limitations:
    # - when fields are present in the local scheme that are not available in the remote scheme, the sync will fail
    # - passwords are not synced

    remote_sync = frappe.get_single("Remote Sync Options")
    remote_source = f"{remote_sync.remote_instance}"
    remote_authorization = remote_sync.get_password('authorization')
    url = f"{remote_source}/api/method/frappe_dev.tmf_toolbox.utils.execute_db_query"
    exclude_tables = ['DATEV Settings']
    #include_tables = ['Singles']
    include_tables = ['Series']
    exclude_modules = ["tmf toolbox","Core", "Custom", "Data Migration", "Desk", "Email", "Integrations","Agriculture","Education","Healthcare","Hotels","Restaurant"]
    tables = frappe.get_list("DocType", fields=["name"], filters={"module": ["not in", exclude_modules],"isSingle": "No"})
    for include in include_tables:
        tables.extend([{'name': include}])
    for x in tables:
        if x["name"] in exclude_tables:
            continue
        tableName = "tab"+x["name"]
        fields = set([c.name for c in frappe.db.get_table_columns_description(tableName)])
        fields = ','.join("`" + field + "`" for field in fields)
        query = """select {fields} from `{table}`""".format(fields=fields,table=tableName)
        headers = {
        'Authorization': f"token {remote_authorization}",
        'Content-Type': 'application/json'
        }
        payload = json.dumps({"query": query})
        response = requests.request("POST", url, headers=headers, data=payload)
        #print(response.json())
        if response.status_code == 200 and response.json()['message']:
            for record in response.json()['message']:
                values = str(record)
                values = values.replace("None,","NULL,")
                values = values.replace(", None",", NULL")
                values = values.replace("[","",1)
                values = values[:-1]
                insert_query = """REPLACE INTO `{table}` ({fields}) VALUES ({values})""".format(table=tableName, fields=fields,values=values)
                #print(insert_query)
                frappe.db.sql(insert_query)
                frappe.db.commit()
        elif response.status_code != 200:
            print("Could not fetch data from remote for table: `" + tableName + "`")
            print("Query was: " + query)
    return("Synced")

@frappe.whitelist()
def execute_db_query(query):
    return(frappe.db.sql(query))


@frappe.whitelist()
def sync_with_remote_enqueue():
    frappe.enqueue(
				queue="short",
				method="frappe_dev.tmf_toolbox.utils.sync_with_remote")