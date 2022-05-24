# -*- coding: utf-8 -*-
{
    'name': "客户资源管理",

    'summary': """
        帮助汽修行业记录&维系客户，并对已完成业务的客户进行记录跟踪
        客户信息&维修记录&零部件管理&历史跟进
        """,

    'description': """
        汽修行业管理自己客户的模块
    """,

    'author': "NIGangJun",
    'website': "None",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Application',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/templates.xml',
        'views/views.xml',
        'views/menu.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
