# -*- coding: utf-8 -*-
# ©  2015-2018 Deltatech
# See README.rst file on addons root folder for license details


from odoo import models, fields, api, _



class service_agreement_line(models.Model):
    _inherit = 'service.agreement.line'

    equipment_id = fields.Many2one('service.equipment', string='Apartment', index=True)



class service_consumption(models.Model):
    _inherit = 'service.consumption'

    equipment_id = fields.Many2one('service.equipment', string='Apartment', index=True)


