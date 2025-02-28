from odoo import models, fields, api

class MyModel(models.Model):
    _name = 'my.custom.model'
    _description = 'My Custom Model'

    name = fields.Char(string="Name")
    email = fields.Char(string="Email")
    
    def send_email_template(self):
        print("method calling.................")
        for record in self:
            print(f"Sending email to: {record.email}")
            template = self.env.ref('custom_product_report.my_email_template')
            print("method inside temp............")
            if template:
                print("method inside for if ............")
                template.send_mail(record.id, force_send=True)
                print("method out ............")                
