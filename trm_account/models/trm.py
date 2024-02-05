# Importa las clases necesarias desde el módulo 'odoo'
from odoo import models, fields, api

# Define tu modelo 'Trm' que hereda del modelo 'account.move'
class Trm(models.Model):
    _inherit = 'account.move'

    # Definición de campos adicionales
    trm_date = fields.Date('TRM Date', default=fields.Date.today())
    trm_value = fields.Float('TRM Value', readonly=True, compute='_compute_trm_value', store=True)
    currency_id = fields.Many2one('res.currency', string='Main Currency', domain="[('active', '=', True)]")
    from_currency_id = fields.Many2one('res.currency', string='Currency', domain="[('active', '=', True)]")

    # Relación uno a muchos con 'account.move.line'
    invoice_line_ids = fields.One2many('account.move.line', 'move_id', string='Invoice Lines')
    
    # Método para calcular el valor de TRM
    @api.depends('trm_date', 'from_currency_id', 'currency_id')
    def _compute_trm_value(self):
        for record in self:
            if record.currency_id and record.from_currency_id and record.currency_id != record.from_currency_id:
                rate = record.from_currency_id._get_conversion_rate(to_currency=record.currency_id,
                                                                    from_currency=record.from_currency_id,
                                                                    date=record.trm_date,
                                                                    company=record.company_id)
            
                record.trm_value = rate if rate else 0.0
            else:
                record.trm_value = 0.0
                
    # Método que se ejecuta al cambiar la moneda de origen
    @api.onchange('from_currency_id')
    def _onchange_currency_id(self):
        self._compute_trm_value()
        self._update_invoice_lines()

    # Método que se ejecuta al cambiar la fecha de TRM
    @api.onchange('trm_date')
    def _onchange_trm_date(self):
        self._compute_trm_value()
        self._update_invoice_lines()
        
    # Método que se ejecuta al cambiar la moneda principal
    @api.onchange('currency_id')
    def _onchange_currency(self):
        self._compute_trm_value()
        self._update_invoice_lines()

    # Método para actualizar las líneas de factura
    def _update_invoice_lines(self):
        for line in self.invoice_line_ids:
            if self.trm_value != 0.0:
                line.price_unit = line.price_unit * self.trm_value
                line.price_subtotal = line.price_unit * line.quantity * (1 - line.discount / 100.0)
