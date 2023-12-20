{
    'name': "trm_account",
    'description': """
        Get all TRM by date
    """,
    'author': "Cristian Berrio",
    'category': 'Invoice',
    'version': '1',
    'depends': ['base', 'account'],
    'data': [
        'views/views.xml',
        'views/report_invoice_document.xml'
    ],
    'installable': True,
    'auto_install': False,
    'license': "LGPL-3",
}
