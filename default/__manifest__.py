{
    'name': 'Default Form',
    'version': '17.0.1.0.0',
    'category': 'Default Form',
    'summary': 'Default Form Related Module',
    'description': """
    This module contains all the common features of Default Form.
    """,
    'depends': ['base','web','sale_management','account'],
    'data': [
        'security/ir.model.access.csv',
        'views/default_view.xml',
        'views/assets.xml',
        'views/widget_popup.xml',
        'views/widget_sale.xml',
        'views/term_con.xml',
        # 'reports/account_invoice_acction.xml',
        'reports/account_invoice_temp.xml',
        'views/account_invoice_view.xml',
        'views/page_pra_view.xml',
        'views/add_service_view.xml',
        'views/menu_template.xml'
        ],

    'demo': [],
    'installable': True,
    'assets': {
        'web.assets_backend': [
            '/default/static/src/js/my_component.js',
            '/default/static/xml/templates.xml',
            '/default/static/xml/widget_temp.xml',
            '/default/static/src/js/widget_popup.js',
            '/default/static/src/js/sale_widget.js',
            '/default/static/xml/widget_sale_temp.xml',
            'default/static/src/js/term_condition.js',
            'default/static/xml/term_condition_temp.xml',
            'default/static/src/js/page_pra.js',
            'default/static/xml/page_pra_temp.xml'
        ]
    },
    'images': [
        'static/image/icon.png'
    ],
    'controllers': ['controllers'],
    'installable': True,
    'license': 'LGPL-3',
}