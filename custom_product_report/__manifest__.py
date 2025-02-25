{
    'name': 'Custom Product Report',
    'version': '17.0.1.0.0',
    'category': 'Sales',
    'summary': 'Generate PDF reports for product details',
    'description': """
    custom gift.
    """,
    'depends': ['base', 'sale_management'],
    'data': [
        'security/ir.model.access.csv',
        'views/product_report.xml',
        'reports/product_report_action.xml',
        'reports/product_report_template.xml',
        # 'views/sale_form.xml',
        # 'reports/sale_order_act.xml',
        # 'reports/sale_order_temp.xml'
        # 'views/partner_view.xml',
        # 'reports/purchase_temp.xml',
        # 'reports/purchase_act.xml',
        # 'views/purchase_report.xml',
        ],
    'demo': [],
    'installable': True,
    'assets': {},
    'license': 'LGPL-3',
}