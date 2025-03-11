from odoo import models, fields
from openpyxl import Workbook
from io import BytesIO
import base64

class ActivityAnalysis(models.Model): 
    _name = 'activity.analysis'
    _description = 'Action'

    name = fields.Many2one('res.partner', string='Student Name')
    add_date = fields.Datetime(string='Addmission Date')
    addr = fields.Text (string='Address')
    email = fields.Char(strong='Email')
    phone = fields.Char(string='Phone')
    age = fields.Integer(string='Age')
    last_pass = fields.Selection([
        ('10TH', '10TH'),
        ('12TH', '12TH'),
        ('Bechlore', 'Bechlore'),
        ('Master', 'Master'),
        ('Phd', 'Phd')
    ], string='Last Pass Out')
    stream = fields.Selection([
        ('10Th','10Th'),
        ('Science', 'Science'),
        ('Commerce', 'Commerce'),
        ('Arts', 'Arts')],
        string='Stream')
    
    #this is for all inserted record's values print in xml 
    def all_generate_xlsx_report(self):
        workbook = Workbook()
        sheet = workbook.active
        sheet.title = 'All Activity Analysis Report'
        sheet.append(['Student Name','Addmission Date', 'Address', 'Email', 'Phone', 'Age', 'Last Pass Out', 'Stream'])

        records = self.env['activity.analysis'].search([]) 

        for record in records:
            sheet.append([
                record.name.name if record.name else 'N/A',  
                record.add_date if record.add_date else 'N/A',
                record.addr if record.addr else 'N/A',
                record.email if record.email else 'N/A',
                record.phone if record.phone else 'N/A',
                record.age if record.age else 'N/A',
                record.last_pass if record.last_pass else 'N/A',
                record.stream if record.stream else 'N/A'
            ])

        file_stream = BytesIO()
        workbook.save(file_stream)
        file_stream.seek(0)

        file_data = base64.b64encode(file_stream.read()).decode('utf-8')

        attachment_record = self.env['ir.attachment'].create({
            'name': 'activity_analysis_report.xlsx',
            'type': 'binary',
            'datas': file_data,
            'store_fname': 'activity_analysis_report.xlsx',
            'mimetype': 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
        })

        return {
            'type': 'ir.actions.act_url',
            'url': '/web/content/%s?download=true' % attachment_record.id,
            'target': 'self',
        }

    #this is for current which we open only 1 record's values print in xml
    def generate_xlsx_report(self):
        # We are using 'self' to refer to the current record.
        record = self

        # Create a new workbook and add a sheet
        workbook = Workbook()
        sheet = workbook.active
        sheet.title = 'Activity Analysis Report'
        
        # Add header row
        sheet.append(['Student Name', 'Admission Date', 'Address', 'Email', 'Phone', 'Age', 'Last Pass Out', 'Stream'])
        # Extract fields and make sure you get primitive values
        sheet.append([
            record.name.name if record.name.name else 'N/A', 
            record.add_date if record.add_date else 'N/A',
            record.addr if record.addr else 'N/A',
            record.email if record.email else 'N/A',
            record.phone if record.phone else 'N/A',
            record.age if record.age else 'N/A',
            record.last_pass if record.last_pass else 'N/A',
            record.stream if record.stream else 'N/A'
        ])

        # Save the workbook to a BytesIO stream
        file_stream = BytesIO()
        workbook.save(file_stream)
        file_stream.seek(0)

        # Encode the file to base64
        file_data = base64.b64encode(file_stream.read()).decode('utf-8')

        # Create an attachment for the report
        attachment_record = self.env['ir.attachment'].create({
            'name': f'{record.name}_activity_analysis_report.xlsx',
            'type': 'binary',
            'datas': file_data,
            'store_fname': f'{record.name}_activity_analysis_report.xlsx',
            'mimetype': 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
        })

        # Provide the download link for the generated file
        return {
            'type': 'ir.actions.act_url',
            'url': f'/web/content/{attachment_record.id}?download=true',
            'target': 'self',
        }