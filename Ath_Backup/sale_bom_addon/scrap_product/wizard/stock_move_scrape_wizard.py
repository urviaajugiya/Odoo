from odoo import models, fields, api

class StockMoveScrapeWizard(models.Model):
    _name = 'stock.move.scrape.wizard'
    _description = 'Scrape Wizard for Stock Move Lines'

    production_id = fields.Many2one('mrp.production', string='Production Order', readonly=True)
    move_line_ids = fields.One2many('stock.move.scrape.line', 'wizard_id', string='Move Lines')

    @api.model
    def default_get(self, fields_list):
        res = super().default_get(fields_list)
        active_id = self.env.context.get('active_id')
        if active_id:
            mrp = self.env['mrp.production'].browse(active_id)
            move_lines_data = []
            for move in mrp.move_raw_ids:
                for line in move.move_line_ids:
                    # print(move.move_line_ids)
                    move_lines_data.append((0, 0, {
                        'product_id': line.product_id.id,
                        'location_id': line.location_id.id,
                        'location_dest_id': line.location_dest_id.id,
                        'scrape_qty': 0.0,
                    }))

            res['move_line_ids'] = [(5, 0, 0)] + move_lines_data

        return res

    def action_confirm_scrape(self):
        production = self.env['mrp.production'].browse(self.env.context.get('active_id'))

        for line in self.move_line_ids:
            if line.scrape_qty > 0:
                print(f"Creating scrap for product: {line.product_id.id}, Qty: {line.scrape_qty}")

                scrap = self.env['stock.scrap'].create({
                    'product_id': line.product_id.id,
                    'scrap_qty': line.scrape_qty,
                    'production_id': production.id,
                    'location_id': line.location_id.id,
                    'origin': production.name,
                    # 'scrap_location_id':,
                    'company_id': production.company_id.id
                })


                scrap.action_validate()

                # print(scrap.production_id.move_raw_ids)
                # for rec in scrap.production_id.move_raw_ids:
                #     if rec.product_id == scrap.product_id:
                #         rec.quantity = rec.quantity - scrap.scrap_qty
                #
                # val = scrap.production_id.move_raw_ids.filtered(lambda m: m.product_id == scrap.product_id)
                # val.quantity -= scrap.scrap_qty

                scrap.production_id.move_raw_ids.filtered(lambda m: m.product_id == scrap.product_id).quantity -= scrap.scrap_qty

                # print(sum(scrap.production_id.move_raw_ids.mapped('product_uom_qty')))
        # team.assignment_max = sum(member.assignment_max for member in team.crm_team_member_ids)

        print("Order placed in scrap")
        return {'type': 'ir.actions.act_window_close'}

