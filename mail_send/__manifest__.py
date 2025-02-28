{
    'name': 'Custom Product Report',
    'version': '17.0.1.0.0',
    'category': 'Sales',
    'summary': 'Generate PDF reports for product details',
    'description': """
    custom gift.
    """,
    'depends': ['base','mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/my_model_view.xml',
        'data/email_template.xml'
        ],
    'demo': [],
    'installable': True,
    'assets': {},
    'license': 'LGPL-3',
}