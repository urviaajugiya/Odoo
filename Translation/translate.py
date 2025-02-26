from odoo import models, fields, api, _  
from datetime import date
from odoo.exceptions import UserError

class translate(models.Model):
    _name = 'translate.info'
    _description = 'Transamission'

    name=fields.Char(string="name")
    pro_name = fields.Char(string=_("Product Name"))
    description = fields.Text(string=_("Product Description"))
    birthdate = fields.Date('Birthdate')
    age = fields.Integer(string=_("Age"), compute='_onchange_')
    check = fields.Integer(string=_("check"),compute="_check_age")

    @api.onchange('age')
    def _check_age(self):
        for record in self:
            if record.age < 15:
                return {
                    'warning': {
                        'title': _('Age Warning'),  
                        'message': _('The age you entered is less than 15. Please verify.')  
                    }
                }
            else:
                record.age = 0

    @api.onchange('birthdate')
    def _onchange_(self):
        for record in self:
            if record.birthdate:
                birthdate = fields.Date.from_string(record.birthdate)
                today = date.today()
                age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
                record.age = age
            else:
                record.age = 0