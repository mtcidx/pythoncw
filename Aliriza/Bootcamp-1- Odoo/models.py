from odoo import models, fields

class BootcampEvent(models.Model):
    _name = 'event.event'
    _inherit = 'event.event'

    price = fields.Float(string='Price',required=True)
    description = fields.Text(string="Description", required = False)