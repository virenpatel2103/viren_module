from odoo import *
from odoo.exceptions import ValidationError


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    # combo_id = fields.Many2one('product.combo', string="Select combo")
    combo_id = fields.Many2one('product.combo', string="Select combo")

    @api.onchange('combo_id')
    def _onchange_combo_id(self):
        for rec in self:
            self.order_line = False
            if rec.combo_id != False:
                line_model_data = self.env['sale.order.line']
                for products in rec.combo_id.sub_product_ids:
                    vals = {
                        'order_id': self.id,
                        'product_id': products.id
                    }
                    new_record = line_model_data.new(vals)
                    new_record.product_id_change()
                    line_model_data.write(vals)


    def action_split_delivery(self):
        for rec in self:
            print('\n\n\n\n\n\n\n')
            print(rec.picking_ids)
            print('\n\n\n\n\n\n\n')
            username = rec.partner_id.id
            lst = []
            for lines in rec.order_line:
                lst.append((0, 0, {'product_id': lines.product_id.id}))

            return {
                "type": "ir.actions.act_window",
                "res_model": "split.delivery",
                "name": "Split delivery wizard",
                "view_mode": "form",
                "target": "new",
                "context": {
                    'default_user_id': username,
                    'default_product_product_ids': lst,
                    'sale_order_id': self.id
            }
        }