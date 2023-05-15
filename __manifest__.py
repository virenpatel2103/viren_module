{
    'name': "Viren module",
    "summary":"Viren module",
    "description": "",
    "version": "15.0.0.1.0",
    "category": "Management",
    "website": "",
    "depends": ['sale'],
    "data": [
        'security/ir.model.access.csv',
        'views/inherit_sale_order_model.xml',
        'views/product_combo_view.xml',
        # 'views/website_layout_view.xml',
    ],
    "demo": [],
    "qweb": [],
    'installable': True,
    'application': True,
    'auto_install': False,

}
