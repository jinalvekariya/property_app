from . import __version__ as app_version

app_name = "property_app"
app_title = "Property App"
app_publisher = "Jinal Balar"
app_description = "Property Management System"
app_email = "vekariyajinal7@gmail.com"
app_license = "MIT"
app_logo_url = "/assets/property_app/img/Propertylogo.png"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
app_include_css = "/assets/property_app/css/propertyapp.css"
# app_include_js = "/assets/property_app/js/property_app.js"

# include js, css files in header of web template
web_include_css = "/assets/property_app/css/propertyapp.css"
# web_include_js = "/assets/property_app/js/property_app.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "property_app/public/scss/website"

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
#	"methods": "property_app.utils.jinja_methods",
#	"filters": "property_app.utils.jinja_filters"
# }

# Installation
# --------
# ----

# before_install = "property_app.install.before_install"
# after_install = "property_app.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "property_app.uninstall.before_uninstall"
# after_uninstall = "property_app.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "property_app.notifications.get_notification_config"

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

scheduler_events = {
    
    "cron": {
        "* * * * *": [
            "property_app.templates.scheduler.update_lease_agreements"
        ]
    },
	# "all": [
	# 	"property_app.tasks.all"
	# ],
	# "daily": [
	# 	"property_app.tasks.daily"
	# ],
	# "hourly": [
	# 	"property_app.tasks.hourly"
	# ],
	# "weekly": [
	# 	"property_app.tasks.weekly"
	# ],
	# "monthly": [
	# 	"property_app.tasks.monthly"
	# ],
    # "yearly": [
    #     "property_app.templates.scheduler.update_lease_agreements"
    # ],
}

# Fixtures
fixtures = [{"dt":"Website Slideshow"} ,  
            {"dt":"Website Settings"},
            {"dt":"Web Page"},
            {"dt":"Navbar Settings"},
            {"dt":"Role" , "filters": [["name", "in", ["Property Manager","Maintenance Staff","Tenant"]]]},
            {"dt":"Workflow","filters":[["name","in", ["Property Leasing", "Maintenance Request Submitting"]]]},
            {"dt":"Workflow State"}]

website_context = {
    "favicon": "/assets/property_app/img/Propertylogo.png",
    "app_logo": "/assets/property_app/img/Propertylogo.png",
    "footer_logo": "/assets/property_app/img/Propertylogo.png",
    "banner_image": "/assets/property_app/img/Propertylogo.png",
}

# Testing
# -------

# before_tests = "property_app.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "property_app.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "property_app.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["property_app.utils.before_request"]
# after_request = ["property_app.utils.after_request"]

# Job Events
# ----------
# before_job = ["property_app.utils.before_job"]
# after_job = ["property_app.utils.after_job"]

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
#	"property_app.auth.validate"
# ]
