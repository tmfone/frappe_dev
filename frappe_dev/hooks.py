from . import __version__ as app_version

app_name = "frappe_dev"
app_title = "Frappe Development Tools"
app_publisher = "tmf.one"
app_description = "Tools to help develop custom apps"
app_email = "info@tmf.one"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/frappe_dev/css/frappe_dev.css"
# app_include_js = "/assets/frappe_dev/js/frappe_dev.js"

# include js, css files in header of web template
# web_include_css = "/assets/frappe_dev/css/frappe_dev.css"
# web_include_js = "/assets/frappe_dev/js/frappe_dev.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "frappe_dev/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
#	"methods": "frappe_dev.utils.jinja_methods",
#	"filters": "frappe_dev.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "frappe_dev.install.before_install"
# after_install = "frappe_dev.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "frappe_dev.uninstall.before_uninstall"
# after_uninstall = "frappe_dev.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "frappe_dev.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
#	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
#	"*": {
#		"on_update": "method",
#		"on_cancel": "method",
#		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"frappe_dev.tasks.all"
#	],
#	"daily": [
#		"frappe_dev.tasks.daily"
#	],
#	"hourly": [
#		"frappe_dev.tasks.hourly"
#	],
#	"weekly": [
#		"frappe_dev.tasks.weekly"
#	],
#	"monthly": [
#		"frappe_dev.tasks.monthly"
#	],
# }

# Testing
# -------

# before_tests = "frappe_dev.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "frappe_dev.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "frappe_dev.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]


# User Data Protection
# --------------------

# user_data_fields = [
#	{
#		"doctype": "{doctype_1}",
#		"filter_by": "{filter_by}",
#		"redact_fields": ["{field_1}", "{field_2}"],
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_2}",
#		"filter_by": "{filter_by}",
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_3}",
#		"strict": False,
#	},
#	{
#		"doctype": "{doctype_4}"
#	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"frappe_dev.auth.validate"
# ]
