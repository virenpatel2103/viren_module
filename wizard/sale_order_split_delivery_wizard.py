from odoo import fields, api, models


class SplitDeliveryWizard(models.TransientModel):
    _name = 'split.delivery'
    _description = 'Split delivery'
    _rec_name = 'id'

    user_id = fields.Many2one('res.partner', string="Customer")
    product_product_ids = fields.One2many('split.product', 'ref_id',
                                          string="Details")

    def action_confirm(self):
        stock_data = self.env['stock.picking'].search \
            ([('sale_id', '=', self._context['sale_order_id'])])


    class SplitProduct(models.TransientModel):
        _name = 'split.product'

        ref_id = fields.Many2one('split.delivery', string="")
        product_id = fields.Many2one('product.product', string='Product')
        split_choice = fields.Boolean(string="Split")

        @api.onchange('split_choice')
        def _onchange_split_choice(self):
            print(self._context)



