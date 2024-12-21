# Import necessary classes from the 'odoo' module
from odoo import models, fields

# Define your 'AccountMove' model which inherits from the 'account.move' model
class AccountMove(models.Model):
    _inherit = 'account.move'
