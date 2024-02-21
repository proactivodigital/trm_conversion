{
    'name': "trm_account",
    'description': """
        Get all TRM by date
    """,
    'author': "Cristian Berrio",
    'category': 'Invoice',
    'version': '17.1',
    'depends': ['base', 'account', 'sale'],
    'data': [
        'views/views.xml',
        'views/view_subscription.xml',
        'views/report_invoice_document.xml',
        'views/report_subscription_document.xml'
    ],
    'installable': True,
    'auto_install': False,
    'license': "LGPL-3",
}
