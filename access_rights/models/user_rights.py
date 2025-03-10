from odoo import models, fields, api

class UserRights(models.Model):
    _name = 'user.rights'
    _description = 'User Rights'

    name = fields.Many2one('res.users')
    product_id_read = fields.Many2one('product.product', string='Product')
    description = fields.Char(string='Only Authority Use')
    payment_term = fields.Selection([
        ('immediate payment', 'Immediate Payment'),
        ('15 days', '15 Days'),
        ('21 days', '21 Days'),
        ('45 days', '45 Days'),
        ('end of the following month', 'End of the Following Month')
    ], string='Payment Term')