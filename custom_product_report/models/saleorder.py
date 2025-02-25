from odoo import models, fields, api

class saleorder(models.Model): #soldto soldto
    _inherit = 'sale.order'

    select = fields.Char(string="select your order")
    comment = fields.Char(string="Comment")