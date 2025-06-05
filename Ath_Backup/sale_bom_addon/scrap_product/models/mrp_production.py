from odoo import models, fields, api

class MrpProduction(models.Model):
        _inherit = 'mrp.production'

        # production_id = fields.Many2one('mrp.production', string='production ids')

        # def action_open_scrap_wizard(self):
        #     self.ensure_one()
        #     return {
        #         'type': 'ir.actions.act_window',
        #         'name': 'Scrap Products',
        #         # 'res_model': 'stock.scrap',
        #         'res_model' : 'stock.move',
        #         'view_mode': 'form',
        #         'target': 'new',
        #         'context': {
        #             # 'default_production_id': self.id,
        #             'default_product_id': self.product_id.id,
        #             # 'default_origin': self.name,
        #             'default_location_id': self.location_src_id.id,
        #             'default_quantity': self.product_qty,
        #             # 'default_company_id': self.company_id.id,
        #         }
        #     }

        def open_scrape_wizard(self):
            return {
                'name': 'Scrape Wizard',
                'type': 'ir.actions.act_window',
                'res_model': 'stock.move.scrape.wizard',
                'view_mode': 'form',
                'target': 'new',
                'context': {
                    'active_id': self.id,
                }
            }
