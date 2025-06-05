from odoo import fields, models, api


class StockScrap(models.Model):
    _inherit = 'stock.scrap'

    def write(self,vals):
        res = super(StockScrap, self).write(vals)
        print("hiiiiiiii")
        return res