# Importa las clases necesarias desde el módulo 'odoo'
from odoo import models, fields

# Define tu modelo 'AccountMove' que hereda del modelo 'account.move'
class AccountMove(models.Model):
    _inherit = 'account.move'
