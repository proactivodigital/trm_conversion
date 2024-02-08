from odoo import models, fields, api
from odoo.tools import DEFAULT_SERVER_DATE_FORMAT
from datetime import datetime

class TrmSubscription(models.Model):
    _inherit = 'sale.order'

    trm_date = fields.Date('TRM Date', default=fields.Date.today())
    trm_value = fields.Float('TRM Value', readonly=True, compute='_compute_trm_value', store=True)
    from_currency_id = fields.Many2one('res.currency', string='From Currency', domain="[('active', '=', True)]")
    to_currency_id = fields.Many2one('res.currency', string='To Currency', domain="[('active', '=', True)]")

    # Método para calcular el valor de TRM
    @api.depends('trm_date', 'from_currency_id', 'to_currency_id')
    def _compute_trm_value(self):
        for record in self:
            if record.to_currency_id and record.from_currency_id and record.to_currency_id != record.from_currency_id:
                rate = record.from_currency_id._get_conversion_rate(to_currency=record.to_currency_id,
                                                                    from_currency=record.from_currency_id,
                                                                    date=record.trm_date,
                                                                    company=record.company_id)
            
                record.trm_value = rate if rate else 0.0
            else:
                record.trm_value = 0.0
        
    # Método que se ejecuta al cambiar la moneda principal
    @api.onchange('to_currency_id')
    def _onchange_currency(self):
        self._compute_trm_value()
        self._update_invoice_lines()

    def _update_invoice_lines(self):
        if self.trm_value != 0.0:
            for line in self.order_line:
                line.price_unit = line.price_unit * self.trm_value
                line.price_subtotal = line.price_subtotal * self.trm_value
