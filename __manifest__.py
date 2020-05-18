# -*- coding: utf-8 -*-
{
    'name': "school",

    'summary': """
       School MAngment""",

    'description': """
        School MAngment 
           """,

    'author': "Moaz",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/school_security_view.xml',
        'security/ir.model.access.csv',
        'data/student_sequence.xml',
        'data/teacher_sequence.xml',
        'data/subject_sequence.xml',
        'views/school_menu_view.xml',
        'views/school_parents_view.xml',
        'views/school_student_view.xml',
        'views/school_teacher_view.xml',
        'views/school_degree_view.xml',
        'views/school_subject_view.xml',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}