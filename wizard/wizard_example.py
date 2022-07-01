from odoo import fields, models


class WizardExample(models.TransientModel):
    _name = 'wizard.example'
    _description = 'Example Wizard'

    date_from = fields.Date(string="Date from")
    date_to = fields.Date(string="Date to")
    name = fields.Char(string="Name")
