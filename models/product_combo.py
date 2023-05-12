from odoo import *
# from odoo.exceptions import ValidationError


class ProductCombo(models.Model):
    _name = "product.combo"
    _rec_name = "name"

    name = fields.Char(string="Combo name")
    sub_product_ids = fields.Many2many('product.template', string="Select products")