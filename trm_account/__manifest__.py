{
    'name': "trm_account",
    'description': """
        Get all TRM by date
    """,
    'summary': """
        Get all TRM by date
    """,
    'author': "Cristian Berrio",
    'category': 'Invoice',
    'version': '17.0.22.08.031410',
    'depends': ['base', 'account', 'sale'],
    'data': [
        'views/views.xml',
        'views/report_invoice_document.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
    'license': "GPL-3",
}