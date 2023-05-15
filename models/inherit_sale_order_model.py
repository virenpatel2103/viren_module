from odoo import *
from odoo.exceptions import ValidationError


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    # combo_id = fields.Many2one('product.combo', string="Select combo")
    combo_id = fields.Many2one('product.combo', string="Select combo")

    @api.onchange('combo_id')
    def _onchange_combo_id(self):
        for rec in self:
            if rec.order_line == False:
                print('----------------------------')
            else:
                print('***************************')
                if rec.combo_id != False:
                    data_search = self.env['product.combo'].search([('id', '=', rec.combo_id.id)])
                    lst = []
                    for line in data_search.sub_product_ids:
                        lst.append((0,0, {'product_id': line.id}))