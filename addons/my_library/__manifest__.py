# -*- coding: utf-8 -*-
{
    'name': "My Library",  # Module title
    'summary': "Manage books and movies easily",  # Module subtitle phrase
    'description': """
Manage Library
==============
Description related to library.
    """,  # Supports reStructuredText(RST) format
    'author': "Parth Gajjar",
    'website': "http://www.example.com",
    'category': 'Tools',
    'version': '15.0.1',
    'depends': ['base', 'website'],

    'data': [
        'security/groups.xml',
        'security/ir.model.access.csv',
        'views/library_book.xml',
        'views/library_movie.xml',
        'views/templates.xml',

    ],

    # This demo data files will be loaded if db initialize with demo data (commented because file is not added in this example)
    # 'demo': [
    #     'demo.xml'
    # ],
   # 'assets': {
   #     "web.assets_backend": ["path to .js or css, like /module_name/static/src/...",...],
   #     "web.assets_qweb": ["path to .xml, like /module_name/static/src/...",...],

    # },
    #'assets': {
    #    'web.assets_backend': [
    #        'my_library/static/src/**/*',
    #    ],
    #    'web.assets_qweb': [
    #        'my_library/static/src/**/*',
    #    ],
    #},
    'assets': {
        'web.assets_backend': [
            'my_library/static/src/**/*',
        ],
        'web.assets_qweb': [
            'my_library/static/src/**/*',
        ],
        'web.qunit_suite_tests': [
            'my_library/static/tests/colorpicker_tests.js',

        ],

    },

    'installable': True,

    "application": True,
}



