from odoo import models, fields, api
from odoo.tools import DEFAULT_SERVER_DATE_FORMAT
from datetime import datetime

class TrmSubscription(models.Model):
    _inherit = 'sale.order'

    trm_date = fields.Date('TRM Date', default=fields.Date.today(), readonly=True, states={'draft': [('readonly', False)]})
    trm_value = fields.Float('2.00')
    currency_id = fields.Many2one('res.currency', string='Main Currency', domain="[('active', '=', True)]")