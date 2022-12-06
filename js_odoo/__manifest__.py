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
        
        #'security/security.xml',
        #'security/ir.model.access.csv',
        'views/assets.xml',
                   
    ],

    'qweb': [
        'static/src/xml/tree_button.xml',
    ],

    'installable': True
}
