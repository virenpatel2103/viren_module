from odoo import *
from odoo.exceptions import ValidationError


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    # combo_id = fields.Many2one('product.combo', string="Select combo")
    combo_id = fields.Char("iiiinnnnnhhheerriit")

#




