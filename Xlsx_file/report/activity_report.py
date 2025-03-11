from odoo import models

class ActivityReport(models.AbstractModel):
    _name = 'report.action_module.view_activity_analysis'
    _description = 'Activity Analysis XLSX Report'

    def generate_xlsx_report(self, data, partners):
        return partners.generate_xlsx_report()