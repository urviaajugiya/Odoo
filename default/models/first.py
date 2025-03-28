from odoo import models, fields, api

class first(models.Model):
    _name = 'first.model'
    _description ='Form'
    _rec_name = 'my_model_id'

    name = fields.Char('Name')
    my_model_id = fields.Many2one('my.model', string='Related Record')
      
class MyModel(models.Model):
    _name = 'my.model'

    name = fields.Char(string='Name')
    description = fields.Text(string='Description')
    active = fields.Boolean(default=True)
    status = fields.Selection([
        ('draft', 'Draft'),
        ('active', 'Active'),
        ('inactive', 'Inactive')
    ], string='Status', default='draft')

    @api.depends('name', 'status') 
    def _compute_display_name(self):
        for record in self:
            if record.name and record.status:
                record.display_name = f"{record.name} ({record.status})"
            else:
                record.display_name = 'Unknown'