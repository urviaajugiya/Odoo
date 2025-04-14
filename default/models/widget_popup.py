from odoo import models, fields

class MyModel(models.Model):
    _name = 'widget.popup'

    name = fields.Char(string='Name')
    description = fields.Text(string='Description')
    active = fields.Boolean(default=True)
    status = fields.Selection([
        ('draft', 'Draft'),
        ('active', 'Active'),
        ('inactive', 'Inactive')
    ], string='Status', default='draft')