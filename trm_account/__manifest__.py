{
    'name': "trm_account",  # The name of the module
    'description': """
        Get all TRM by date  # Detailed description of the module, explaining that it retrieves the TRM (Representative Market Rate) by date.
    """,
    'summary': """
        Get all TRM by date  # A brief summary of the module, stating the core functionality of getting the TRM by date.
    """,
    'author': "Cristian Berrio",  # The name of the author of the module.
    'category': 'Invoice',  # The category of the module in Odoo. It is classified under 'Invoice' indicating it is related to invoicing.
    'version': '17.0.22.08.031410',  # Version of the module. This is the version number used to manage updates.
    'depends': ['base', 'account', 'sale'],  # Module dependencies. This module requires the 'base', 'account', and 'sale' modules to be installed.
    'data': [
        'views/views.xml',  # Files for the user interface views.
        'views/report_invoice_document.xml',  # Report view files, related to invoice document reporting.
    ],
    'installable': True,  # Indicates whether the module is installable. If True, the module can be installed in Odoo.
    'auto_install': False,  # Indicates whether the module should be automatically installed with other modules. False means it must be installed manually.
    'application': False,  # Defines whether the module is a full-fledged application within Odoo (True if it is an application, False if it is not).
    'license': "GPL-3",  # The license under which the module is distributed (in this case, GPL-3).
}
