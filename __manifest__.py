{
    'name': "mangatheque",

    'summary': "Application de gestion des mangas",

    'description': """
    Cette application vous permet de gérer tous vos mangas. Et c'est aussi ma première app.
    Faite avec le tutoriel de L'informatique sans complexe.
    """,

    'author': "Brakster",
    'website': "https://www.brakster.com/mangatheque-odoo-app",
    
    'application': True,
    'installable' : True,

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Tutorial',
    'version': '19.0.1.0.0',
    'license': 'LGPL-3',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/manga_security.xml',
        'security/ir.model.access.csv',
        #'views/views.xml',
        #'views/templates.xml',
        'views/manga.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

