from odoo import models, fields, api
from odoo.exceptions import ValidationError

class actionmodel(models.Model): 
    _name = 'action.info'
    _description = 'Action'

    name = fields.Char(string='name') 
    ref = fields.Char("Reference",default=lambda self: self.env['ir.sequence'].next_by_code('model.order'),copy=False)
    # order_id = fields.Integer(string="Order Number")
    age = fields.Date(string="Age")

    _sql_constraints = [('name_uniq', 'unique(name)', "Unique  name"),
                        ('positive_total_amount','CHECK(total_amount>0)','the total amount should be greater than 0')]#sql level constraints
    date_order = fields.Datetime(string='Order Date', default=fields.Datetime.now)  
    total_amount = fields.Float(string='Total Amount')  
    customer_id = fields.Many2one('res.partner', string='Customer')
    phone = fields.Char(string="Phone")
    mobile = fields.Char(string="Mobile")
    email_to = fields.Char(string="Email to")
    email_from = fields.Char(string="Email from")
    birthday_date = fields.Date(string="Birthday")
    is_birthday = fields.Boolean(string="Is Birthday Today?", default=False)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('in_consultation', 'In Consultation'),
        ('done', 'Done')
    ], default='draft', string='State')   

    @api.constrains('age')#python level constraints
    def _check_positive_age(self):
        for record in self:
            if record.age and record.age < fields.Date.from_string('1900-01-01') or record.age > fields.Date.from_string('2025-03-04'):
                raise ValidationError('The age should be a reasonable date greater than 1900-01-01 or less than 2025-03-04') 

    def action_done(self): #serveraction
        for record in self:
            record.state = 'done'
    
    def action_copy_phone_to_mobile(self):#serveraction
        for record in self:
            if record.phone and not record.mobile:
                record.write({'mobile': record.phone})

    def check_birthdays(self):#sheduleaction
        today = fields.Date.today()
        birthday_today = self.search([('birthday_date', '=', today)])
        for employee in birthday_today:
            employee.is_birthday = True
            if employee:
                template = self.env.ref('action_module.birthday_email_template')
                if template:
                    template.send_mail(employee.id, force_send=True)
        return True

    # @api.model
    # def create(self,vals_list):
    #     vals_list['ref'] = self.env['ir.sequence'].next_by_code('model.order')
    #     return super().create(vals_list)