from odoo import models,fields

class AccountInvoice(models.Model):
    _inherit = 'account.move'

    select = fields.Char(string="select your order")