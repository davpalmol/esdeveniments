# -*- coding: utf-8 -*-
# from odoo import http


# class Esdeveniments(http.Controller):
#     @http.route('/esdeveniments/esdeveniments', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/esdeveniments/esdeveniments/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('esdeveniments.listing', {
#             'root': '/esdeveniments/esdeveniments',
#             'objects': http.request.env['esdeveniments.esdeveniments'].search([]),
#         })

#     @http.route('/esdeveniments/esdeveniments/objects/<model("esdeveniments.esdeveniments"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('esdeveniments.object', {
#             'object': obj
#         })

