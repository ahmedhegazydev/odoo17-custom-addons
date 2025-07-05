from odoo import models, fields

class Greeting(models.Model):
    _name = 'hello.greeting'
    _description = 'Greeting Model'

    name = fields.Char(string='Name', required=True)
    message = fields.Text(string='Message')
