from odoo import models, fields
from odoo.exceptions import AccessError

class user_role(models.Model):
    _name = 'user.role'
    _description = 'User Role'

    name = fields.Many2one(string="Country", comodel_name='res.country')
    product_id = fields.Many2one('product.product', string='Product')
    _sql_constraints = [('customer_uniq', 'unique(customer_name)', "Already Exist")]
    description = fields.Char(string='Description')
    customer_id = fields.Char(string='Customer')
