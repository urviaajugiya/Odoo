{
    'name': 'Default Form',
    'version': '17.0.1.0.0',
    'category': 'Default Form',
    'summary': 'Default Form Related Module',
    'description': """
    This module contains all the common features of Default Form.
    """,
    'depends': ['base','web'],
    'data': [
        'security/ir.model.access.csv',
        'views/default_view.xml',
        # 'reports/custom_report_template.xml',
        # 'reports/custom_report_action.xml',
        # 'views/my_component.xml',
        # 'views/js_button.xml',
        'views/assets.xml',
        # 'views/templates.xml'
        ],

    'demo': [],
    'installable': True,
    'assets': {
        'web.assets_backend': [
            '/default/static/src/js/my_component.js',
            '/default/static/xml/templates.xml'
        ]
    },
    'installable': True,
    'license': 'LGPL-3',
}