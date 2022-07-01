# Copyright 2021 - 2022 Pidela.App
{
    'name': "Odoo Wizard",
    'summary': "Odoo Wizard Example",
    'description': """
Odoo Wizard Example
===================
    * Added a Wizard window Contacts app.
    """,
    'author': 'Leonardo J. Caballero G.',
    'website': "https://github.com/macagua",
    'license': "LGPL-3",
    'category': 'Hidden',
    'version': '13.0.1.0.1',
    'data': [
        'wizard/wizard_example_views.xml',
    ],
    'depends': [
        'contacts',
    ],
    'images': ['static/description/icon.png'],
    'post_load': None,
    'pre_init_hook': None,
    'post_init_hook': None,
    'uninstall_hook': None,
    'application': False,
    'auto_install': False,
    'installable': True,
}
