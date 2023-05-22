from odoo import fields, api, models


class SplitDeliveryWizard(models.TransientModel):
    _name = 'split.delivery'
    _description = 'Split delivery'
    _rec_name = 'id'

    user_id = fields.Many2one('res.partner', string="Customer")
    product_product_ids = fields.One2many('split.product', 'ref_id',
                                          string="Details")

    def action_action_confirm(self):
        print(self._context)

        stock_data = self.env['stock.picking'].search \
            ([('sale_id', '=', self._context['sale_order_id'])])
        print(stock_data)
        new_data_one = stock_data.copy({
            'move_ids_without_package': False,
            'sale_id': self._context['sale_order_id']
        })
        print(new_data_one)
        new_data_two = stock_data.copy({
            'move_ids_without_package': False,
            'sale_id': self._context['sale_order_id']
        })
        print()
        print(new_data_two)
        for lines in self.product_product_ids:
            if lines.split_choice == True:
                for rec in stock_data.move_ids_without_package:
                    if rec.product_id == lines.product_id:
                        rec.copy({
                            'picking_id': new_data_one.id
                        })
            else:
                for rec in stock_data.move_ids_without_package:
                    if rec.product_id == lines.product_id:
                        rec.copy({
                            'picking_id': new_data_two.id
                        })

        stock_data.action_cancel()
        new_data_one.action_confirm()
        new_data_two.action_confirm()




    class SplitProduct(models.TransientModel):
        _name = 'split.product'

        ref_id = fields.Many2one('split.delivery', string="")
        product_id = fields.Many2one('product.product', string='Product')
        split_choice = fields.Boolean(string="Split")

        @api.onchange('split_choice')
        def _onchange_split_choice(self):
            print(self._context)



