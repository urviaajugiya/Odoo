from odoo import models, fields, api

class StockMoveScrapeLine(models.Model):
    _name = 'stock.move.scrape.line'
    _description = 'Stock Move Line for Scrape Wizard'

    wizard_id = fields.Many2one('stock.move.scrape.wizard', string='Wizard')
    product_id = fields.Many2one(
        'product.product', 'Product', domain="[('type', '=', 'consu')]",
        required=True, check_company=True,readonly=False)
    # product_id = fields.Many2one('product.product', string='Product', readonly=True)
    location_id = fields.Many2one(
        'stock.location', 'Source Location',
        compute='_compute_location_id', store=True, required=True, precompute=True,
        domain="[('usage', '=', 'internal')]", check_company=True, readonly=False)
    # location_id = fields.Many2one('stock.location', string='Source Location', readonly=True)
    location_dest_id = fields.Many2one('stock.location', string='Destination Location', readonly=True)
    scrape_qty = fields.Float('Scrape Quantity')
