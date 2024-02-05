from odoo import models, fields, api
from odoo.tools import DEFAULT_SERVER_DATE_FORMAT
from datetime import datetime

class TrmSubscription(models.Model):
    _inherit = 'sale.order'

    trm_date = fields.Date('TRM Date', default=fields.Date.today(), readonly=True, states={'draft': [('readonly', False)]})
    trm_value = fields.Float('TRM Value', readonly=True, compute='_compute_trm_value', store=True)
    currency_id = fields.Many2one('res.currency', string='Main Currency', domain="[('active', '=', True)]")

    @api.depends('currency_id', 'trm_date', 'amount_total')
    def _compute_trm_value(self):
        for order in self:
            # Obtén la tasa de cambio para la moneda seleccionada en la fecha actual
            rate = order.currency_id._get_conversion_rate(order.trm_date, company_id=order.company_id.id)

            # Calcula el valor de TRM multiplicando la tasa de cambio por la cantidad deseada
            order.trm_value = rate * order.amount_total
