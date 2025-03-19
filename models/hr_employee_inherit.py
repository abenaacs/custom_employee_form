from odoo import models, fields

class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    # Add new fields
    work_experience_document = fields.Binary(string="Work Experience Document")