# -*- coding: utf-8 -*-
# from odoo import http


# class PartnerManage(http.Controller):
#     @http.route('/partner_manage/partner_manage', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/partner_manage/partner_manage/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('partner_manage.listing', {
#             'root': '/partner_manage/partner_manage',
#             'objects': http.request.env['partner_manage.partner_manage'].search([]),
#         })

#     @http.route('/partner_manage/partner_manage/objects/<model("partner_manage.partner_manage"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('partner_manage.object', {
#             'object': obj
#         })
