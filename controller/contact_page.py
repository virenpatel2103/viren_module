from odoo import *
from odoo.http import request
# from odoo.addons.website_sale.controllers.main import WebsiteSale



class ContactMenu(http.Controller):
    @http.route('/',  type='http', auth="public", method="post", website=True)
    def home_page(self):
        return request.render('viren_module.home_render')


    @http.route('/contacts', type='http', auth="public", method="post", website=True)
    def contact_menu(self):
        print('\n\n\n\n\n----------------------')
        print("in controller of all contacts")
        print('\n\n\n\n\n----------------------')
        contact_search = request.env['res.partner'].search([])
        vals={'records': contact_search}
        return request.render('viren_module.contact_page', vals)

    # @http.route([
    #     '''/shop''',
    #     '''/shop/page/<int:page>''',
    #     '''/shop/category/<model("product.public.category"):category>''',
    #     '''/shop/category/<model("product.public.category"):category>/page/<int:page>'''
    # ], type='http', auth="none", website=True)
    # def shop(self, page=0, category=None, search='', min_price=0.0, max_price=0.0, ppg=False, **post):
    #     print('\n\n\n\nthis is before super')
    #     res = super(ContactMenu, self).shop(page=page, category=category, search=search, min_price=min_price,
    #                                 max_price=max_price, ppg=ppg, **post)
    #     print(post)
    #     return res