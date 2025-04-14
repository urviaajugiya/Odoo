from odoo import models, fields, api

class TermAndCondition(models.Model):
    _name = 'term.condition'
    _description = 'Term And Condition'

    name = fields.Char(string="Name")
    term = fields.Text("Term And Condition")
    
    def get_term(self):
        print("get_term method run...............")
        demo = []
        for record in self:
            demo.append({
                'name': record.name,
                'term': record.term
            })
        print("DEmo ::::::::::::::::::::::::::::::::", demo)
        return demo
