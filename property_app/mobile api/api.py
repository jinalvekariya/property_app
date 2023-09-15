import frappe
import json

@frappe.whitelist(allow_guest=True)
def response(message, data, success, status_code):
    '''method to generates responses of an API
       args:
            message : response message string
            data : json object of the data
            success : True or False depending on the API response
            status_code : status of the request'''
    frappe.clear_messages()
    frappe.local.response["message"] = message
    frappe.local.response["data"] = data
    frappe.local.response["success"] = success
    frappe.local.response["http_status_code"] = status_code
    return


@frappe.whitelist(allow_guest=True, methods="POST")
def login(login_id, password, device_token=None):
    '''API for user login
       args:
            login_id : username/email of the user
            password : user password'''
    try:
        login_manager = frappe.auth.LoginManager()
        login_manager.authenticate(user=login_id, pwd=password)
        login_manager.post_login()

    except frappe.exceptions.AuthenticationError as exception:
        frappe.log_error(frappe.get_traceback())
        return response(exception, {}, False, 417)

    generate_key = generate_keys(frappe.session.user)
    user = frappe.get_doc("User", frappe.session.user)
    roles1 = frappe.get_roles(frappe.session.user)
    roles = [p for p in roles1 if p != "All" and p != "Guest"]
    if device_token:
        add_new_device(login_id, device_token)
    data = {
        "success_key": 1,
        "sid": frappe.session.sid,
        "api_key": user.api_key,
        "api_secret": generate_key,
        "is_active": user.enabled,
        "user_id": user.username,
        "name": user.full_name,
        "user_type": user.user_type,
        "roles": roles
    }
    return response("Authentication Success", data, True, 200)