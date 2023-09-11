# Copyright (c) 2023, Jinal Balar and contributors
# For license information, please see license.txt

import frappe

def execute(filters=None):
    columns = get_columns()
    data = get_maintenance_request(filters)
    message = None
    chart, datasets = generate_chart(data)
    chart_title = "Maintenance Request Chart"

    return columns, data, message, chart, datasets, chart_title

def get_columns():
    columns = [
        {
            "label": "Maintenance Request", 
            "fieldname": "request_title", 
            "fieldtype": "Data", 
        },
        {
            "label": "Status", 
            "fieldname": "status", 
            "fieldtype": "Data"
        },
        {
            "label": "Assigned To", 
            "fieldname": "assigned_to", 
            "fieldtype": "Link", 
            "options": "Maintenance Staff"
        },
    ]
    return columns

def get_maintenance_request(filters=None):
    data = []
    filter_conditions = {}
    
    if filters and filters.get('status'):
        filter_conditions['status'] = filters['status']

    maintenence_request_data = frappe.get_all(
        "Maintenance Request",
        filters=filter_conditions,
        fields=["request_title", "status", "assigned_to"],
    )
    
    for dt in maintenence_request_data:
        row = {
            'request_title': dt.get('request_title'),
            'status': dt.get('status'),
            'assigned_to': dt.get('assigned_to'),
        }
        data.append(row)

    return data

def generate_chart(data):
    status_counts = {
        'Open': 0,
        'In Progress': 0,
        'Closed': 0,
    }
    
    for entry in data:
        if entry['status'] == 'Open':
            status_counts['Open'] += 1
        elif entry['status'] == 'In Progress':
            status_counts['In Progress'] += 1
        elif entry['status'] == 'Closed':
            status_counts['Closed'] += 1
    
    chart = {
        'data': {
            'labels': ['Open', 'In Progress', 'Closed'],
            'datasets': [
                {
                    'name': 'Status',
                    'values': [status_counts['Open'], status_counts['In Progress'], status_counts['Closed']],
                }
            ],
        },
        'type': 'pie',
        'height': 300,
    }
    
    datasets = [
        {
            'name': 'Status',
            'values': [status_counts['Open'], status_counts['In Progress'], status_counts['Closed']],
        }
    ]
    
    return chart, datasets
