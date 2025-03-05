{
    'name': 'Action Module',
    'version': '17.0.1.0.0',
    'category': '',
    'summary': '',
    'description': """
    """,
    'depends': ['mail'],
    'data': [
        'views/action_view.xml',
        'security/ir.model.access.csv',
        "data/ir_action_server.xml",
        'data/ir_birthday_email.xml',
        'data/ir_sequance_data.xml',
        'security/groups.xml',
        'views/product_manager.xml'
        ],
    'demo': [],
    'installable': True,
    'assets': {},
    'license': 'LGPL-3',
}