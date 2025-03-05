# models/product.py
from odoo import models, fields

class Product(models.Model):
    _name = 'product.manager'
    _description = 'Product Manager'

    name = fields.Char('Product Name', required=True)
    product = fields.Char(string='Product Category')
    price = fields.Float('Price', required=True)
