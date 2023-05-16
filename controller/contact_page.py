from odoo import *
from odoo.http import request


class ContactMenu(http.Controller):
    @http.route('/contacts', type='http', auth="public", method="post", website=True)
    def contact_menu(self):
        print('\n\n\n\n\n----------------------')
        print("in controller of all contacts")
        print('\n\n\n\n\n----------------------')
        contact_search = request.env['res.partner'].search([])
        vals={'records': contact_search}
        return request.render('viren_module.contact_page', vals)
