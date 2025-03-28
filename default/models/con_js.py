from odoo import models, fields

class con_js(models.Model):
    _name = 'con.mod'
    _description = 'My Model'

    name = fields.Char(string="Name")
    counter_value = fields.Integer(string="Counter", default=0)