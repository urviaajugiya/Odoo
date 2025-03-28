from odoo import models, fields, api

class CustomReport(models.Model):
    _name = 'custom.report'
    _description = 'Custom Report Model'

    name = fields.Char(string='Report Name', required=True)
    description = fields.Text(string='Description')
    date = fields.Date(string='Date', required=True)
    # item_id = fields.Many2one('product.template',string='Selected Product')
    # item_id = fields.Many2one(comodel_name='product.template', string='Item')
    product_tmpl_id = fields.Many2one('product.template', 'Product Template', readonly=True)

    @api.model
    def _get_report_values(self, docids, data=None):
        # Fetch products from the database
        product_tmpl_id = self.env['product.template'].browse(docids)

        # Return the data to be displayed in the report template
        return {
            'report': product_tmpl_id,
        }