{
    'name': "Viren module",
    "summary": "Viren module",
    "description": "",
    "version": "15.0.0.1.0",
    "category": "Management",
    "website": "",
    "depends": ['sale'],
    "data": [
        'security/ir.model.access.csv',
        'views/inherit_sale_order_model.xml',
        'views/product_combo_view.xml',
        'views/website_layout_view.xml',
        'views/contact_page_view.xml',
        'views/home_render.xml',
        'views/split_product_delivery_action_sale_order.xml',
        'wizard/sale_order_split_delivery_wizard_view.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'viren_module/static/src/scss/contact_page.scss']
    },
    "demo": [],
    "qweb": [],
    'installable': True,
    'application': True,
    'auto_install': False,

}

#
