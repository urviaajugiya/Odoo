{
    'name': 'Action Module',
    'version': '17.0.1.0.0',
    'category': '',
    'summary': '',
    'description': """
    """,
    'depends': ['mail','sale_management','base'],
    'data': [
        'security/ir.model.access.csv',
        'security/groups.xml',
        'views/product_manager.xml',
        'views/sale_order_tags.xml', #give access of odoo's module
        'views/user_role.xml',
        'views/user_rights.xml'
        ],
    'demo': [],
    'installable': True,
    'assets': {},
    'license': 'LGPL-3',
}