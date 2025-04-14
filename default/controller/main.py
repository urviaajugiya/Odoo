from odoo import http
from odoo.http import request

class ServiceController(http.Controller):

    @http.route('/default/models/add.services/get_services', type='json', auth='user')
    def get_services(self):
        services = request.env['add.services'].sudo().search_read([])
        return services
