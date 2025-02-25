from odoo import models, fields, api

class Companyinfo(models.Model): #soldto soldto
    _name = 'company.info'
    _description = 'Sold to'

    name = fields.Char(string='Your Business Name')
    partner_id = fields.Many2one(comodel_name='res.partner',string='Customer Name')
    st_add = fields.Text(string="Street Address")
    post_code = fields.Char(string='City,State/Province,Zip/Post code')
    country=fields.Many2one(comodel_name='res.country',string='Country')

    #invoie
    invoice_no = fields.Char(string="Invoice No")
    date=fields.Date(string="Date")
    your_ref = fields.Char(string="Your Ref")
    our_ref = fields.Char(string="Our Ref")
    credit_term=fields.Char(string="Credit Term")
    attentionto=fields.Many2one(comodel_name='res.partner',string='Contact Person')

    #product
    product_tmpl_id = fields.Many2many('sale.order.line',string='Products')
    # product_categ_id = fields.Many2one('product.template',string='Product Category' )

    # quantity = fields.Integer(string="Quantity")
    # um =fields.Selection([('sets', 'Sets'),
    #                          ('pcs', 'PCS')], string="UM" )
    # unit_price = fields.Float(string="Unit Price")
    # amount = fields.Float(string="Total Price", compute="_compute_total_price", store=True)
        
    # @api.depends('quantity', 'unit_price')
    # def _compute_total_price(self):
    #     for record in self:
    #         if record.quantity and record.unit_price:
    #             record.amount = record.quantity * record.unit_price
    #         else:
    #             record.amount = 0

    #amount
    subtotal = fields.Float(string='Subtotal', compute='_compute_subtotal', store=True)
    # gst = fields.Float("GST", compute='_compute_gst')
    gst_amount = fields.Integer("GST", compute='_compute_gst')
    pst_amount = fields.Float("PST", compute='_compute_pst')
    invoice_total = fields.Float("Invoice Total",compute='_compute_total_invoice')
    balanceduo = fields.Float("Balance Duo")

    @api.depends('subtotal')
    def _compute_subtotal(self):
        for order in self:
            subtotal = sum(line.price_subtotal for line in order.product_tmpl_id)
            order.subtotal = subtotal
    
    @api.depends('gst_amount')
    def _compute_gst(self):
        for order in self:
            gst_rate = 8 # Get the GST rate for the line
            subtotal = sum(line.price_subtotal for line in order.product_tmpl_id)  # Get the untaxed amount for the line
            gst_amount = (gst_rate / 100) * subtotal
            order.gst_amount = gst_amount  # Store the GST amount in the line
    
    @api.depends('pst_amount')
    def _compute_pst(self):
        for order in self:
            pst_rate = 8 # Get the GST rate for the line
            subtotal = sum(line.price_subtotal for line in order.product_tmpl_id)  # Get the untaxed amount for the line
            pst_amount = (pst_rate / 100) * subtotal
            order.pst_amount = pst_amount  # Store the GST amount in the line
    
    @api.depends('subtotal', 'gst_amount', 'pst_amount')
    def _compute_total_invoice(self):
        for invoice in self:
            invoice.invoice_total = invoice.subtotal + invoice.gst_amount + invoice.pst_amount
  
    #comment
    comment= fields.Text(string="Comment")