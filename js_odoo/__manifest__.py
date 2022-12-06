{
    'name': 'JS odoo',

    'version': '14.0.0.0',

    'author': "Luis Felipe Paternina",

    'contributors': ['Luis Felipe Paternina'],

    'website': "",

    'category': 'PoS',

    'depends': [

        'base',
        'base_automation',
        'point_of_sale',

    ],

    'data': [

        'views/assets.xml',
        'views/sale_order.xml',
                   
    ],

    'qweb': [
        'static/src/xml/tree_button.xml',
        'static/src/xml/kanban_button.xml',
    ],

    'installable': True
}
