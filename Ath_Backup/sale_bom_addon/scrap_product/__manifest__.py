{
    'name': "Scrap Product",
    'category': 'Scrape',
    'summary': "",
    'version': '2.0',
    'depends': ['base','sale_management','mrp','stock'],
    'data': [
        'security/ir.model.access.csv',
        'views/mrp_production.xml',
        'wizard/scrape_wizard.xml'
    ],
    'license': 'LGPL-3',
}
