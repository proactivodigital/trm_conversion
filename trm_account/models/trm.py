# Import necessary classes from the 'odoo' module
from odoo import models, fields, api

# Define the 'Trm' model that inherits from the 'account.move' model
class Trm(models.Model):
    _inherit = 'account.move'

    # Definition of additional fields
    trm_date = fields.Date('TRM Date', default=fields.Date.today(), readonly=True, states={'draft': [('readonly', False)]})
    trm_value = fields.Float('TRM Value', readonly=True, compute='_compute_trm_value', store=True)
    currency_id = fields.Many2one('res.currency', string='Main Currency', domain="[('active', '=', True)]")
    from_currency_id = fields.Many2one('res.currency', string='Currency', domain="[('active', '=', True)]")

    # One-to-many relationship with 'account.move.line' (Invoice Lines)
    invoice_line_ids = fields.One2many('account.move.line', 'move_id', string='Invoice Lines')

    # Method to calculate the TRM value (exchange rate)
    @api.depends('trm_date', 'from_currency_id', 'currency_id')
    def _compute_trm_value(self):
        """
        This method computes the TRM (exchange rate) value based on the
        TRM date, the source currency, and the main currency.
        """
        for record in self:
            if record.currency_id and record.from_currency_id and record.currency_id != record.from_currency_id:
                # Fetch the conversion rate from the 'from_currency_id' to 'currency_id' on the given date
                rate = record.from_currency_id._get_conversion_rate(
                    to_currency=record.currency_id,
                    from_currency=record.from_currency_id,
                    date=record.trm_date,
                    company=record.company_id
                )

                # Assign the conversion rate to the TRM value, or 0.0 if no rate is found
                record.trm_value = rate if rate else 0.0
            else:
                # If no valid currencies or the currencies are the same, set TRM value to 0.0
                record.trm_value = 0.0

    # Method triggered when the 'from_currency_id' field is changed
    @api.onchange('from_currency_id')
    def _onchange_currency_id(self):
        """
        This method is executed when the 'from_currency_id' field is changed.
        It updates the TRM value and the invoice lines based on the new currency.
        """
        self._compute_trm_value()
        self._update_invoice_lines()

    # Method triggered when the 'trm_date' field is changed
    @api.onchange('trm_date')
    def _onchange_trm_date(self):
        """
        This method is executed when the 'trm_date' field is changed.
        It updates the TRM value and the invoice lines based on the new date.
        """
        self._compute_trm_value()
        self._update_invoice_lines()

    # Method triggered when the 'currency_id' field is changed
    @api.onchange('currency_id')
    def _onchange_currency(self):
        """
        This method is executed when the 'currency_id' field is changed.
        It updates the TRM value and the invoice lines based on the new currency.
        """
        self._compute_trm_value()
        self._update_invoice_lines()

    # Method to update the invoice lines based on the TRM value
    def _update_invoice_lines(self):
        """
        This method updates the 'price_unit' and 'price_subtotal' of the invoice lines
        based on the computed TRM value. The prices are adjusted according to the TRM value.
        """
        for line in self.invoice_line_ids:
            if self.trm_value != 0.0:
                # Adjust the unit price based on the TRM value
                line.price_unit = line.price_unit * self.trm_value
                # Recalculate the subtotal based on the adjusted price and quantity
                line.price_subtotal = line.price_unit * line.quantity * (1 - line.discount / 100.0)
