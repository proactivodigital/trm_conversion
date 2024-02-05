# Importa las clases necesarias desde el módulo 'odoo'
from odoo import models, fields, api

# Define tu modelo 'Trm' que hereda del modelo 'account.move'
class TrmSubscription(models.Model):
    _inherit = 'sale.order'

    # Definición de campos adicionales
    trm_date = fields.Date('TRM Date', default=fields.Date.today(), readonly=True, states={'draft': [('readonly', False)]})
    trm_value = fields.Float('TRM Value', readonly=True, compute='_compute_trm_value', store=True)
    currency_id = fields.Many2one('res.currency', string='Main Currency', domain="[('active', '=', True)]")
    