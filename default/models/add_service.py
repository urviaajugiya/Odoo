from odoo import models, fields, api

class AddServices(models.Model):
    _name = 'add.services'
    _description = 'Services And Description'

    name = fields.Char(string="Service Name")
    service_des = fields.Text("Service Description")
    
    def get_services(self):
        print("get_services method run...............")
        demo = []
        for record in self:
            demo.append({
                'service_name': record.name,
                'service_des': record.service_des
            })
        print("Services ::::::::::::::::::::::::::::::::", demo)

        return demo 