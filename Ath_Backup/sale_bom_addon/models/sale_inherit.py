from odoo import models, fields, api
# from odoo.exceptions import ValidationError

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    bom_line_ids = fields.One2many('sale.order.bom.line', 'order_id', string='BOM Materials', compute='_compute_bom_lines', store=True,copy=False)

    @api.depends('order_line.product_id', 'order_line.product_uom_qty')
    def _compute_bom_lines(self):
        for order in self:
            bom_lines = []

            bom_line_set = set(bom_lines)
            bom_line_list = list(bom_line_set)
            print(bom_lines)

            for line in order.order_line:
                print(line)
                product = line.product_id
                print(product)
                if not product:
                    continue

                bom = self.env['mrp.bom'].search([
                    ('product_tmpl_id', '=', product.product_tmpl_id.id)
                ],limit=1)
                print(bom)

                if bom:
                  print("component not find")
                  for component in bom.bom_line_ids:
                        print("component",component)
                        bom_line_list.append((0, 0, {
                            'product_id': component.product_id.id,
                            'product_qty': component.product_qty * line.product_uom_qty
                        }))

            # order.bom_line_ids = [(5, 0, 0)] + bom_line_list
            order.bom_line_ids =  [(5, 0, 0)]
            order.bom_line_ids = bom_line_list
            print("bom_line_ids", bom_line_list)



class SaleOrderBomLine(models.Model):
    _name = 'sale.order.bom.line'
    _description = 'Sale Order BOM Line'

    order_id = fields.Many2one('sale.order', string='Order')
    product_id = fields.Many2one('product.product', string='Component')
    product_qty = fields.Float(string='Quantity')