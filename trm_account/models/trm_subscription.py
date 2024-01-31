from odoo import fields, models

class SaleSubscriptionCustom(models.Model):
    _inherit = 'sale.subscription'

    trm_date = fields.Date('TRM Date', default=fields.Date.today(), readonly=True, states={'draft': [('readonly', False)]})
    trm_value = fields.Float('TRM Value', readonly=True, compute='_compute_trm_value', store=True)
