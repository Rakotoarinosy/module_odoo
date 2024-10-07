# -*- coding: utf-8 -*-
# from odoo import http


# class CustomAddons/newModule(http.Controller):
#     @http.route('/custom_addons/new_module/custom_addons/new_module', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/custom_addons/new_module/custom_addons/new_module/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('custom_addons/new_module.listing', {
#             'root': '/custom_addons/new_module/custom_addons/new_module',
#             'objects': http.request.env['custom_addons/new_module.custom_addons/new_module'].search([]),
#         })

#     @http.route('/custom_addons/new_module/custom_addons/new_module/objects/<model("custom_addons/new_module.custom_addons/new_module"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('custom_addons/new_module.object', {
#             'object': obj
#         })

