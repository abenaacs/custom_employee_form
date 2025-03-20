{
    "name": "Employee Customization",
    "version": "1.0",
    'category': 'Human Resources',
    "summary": "Custom file uploads and field removals for Employee module",
    "description": "This module adds custom file upload fields and removes unnecessary fields from the Employee form",
    "author": "Abenezer Nigussie",
    "depends": ['hr'],
    'data': [
        'views/employee_view.xml',
        'security/ir.model.access.csv',
    ],
    "installable": True,
    "application": False,
    'license': 'LGPL-3',
}
