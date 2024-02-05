from odoo import models, fields, api
from odoo.tools import DEFAULT_SERVER_DATE_FORMAT
from datetime import datetime

class TrmSubscription(models.Model):
    _inherit = 'sale.order'

    trm_date = fields.Date('TRM Date', default=fields.Date.today(), readonly=True, states={'draft': [('readonly', False)]})
    trm_value = fields.Float('TRM Value', default='0.0')
    from_currency_id = fields.Many2one('res.currency', string='Currency', domain="[('active', '=', True)]")