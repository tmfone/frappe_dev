import frappe

@frappe.whitelist(allow_guest=True)
def get_whitelisted_methods():
    whitelisted_functions = []
    for e in frappe.whitelisted:
        whitelisted_functions.append(f"{getattr(e, '__module__')}.{getattr(e, '__name__')}")
    return(whitelisted_functions)
