from odoo import models, fields, http


class ProductTemplateInherit(models.Model):
    _inherit ="product.template"
    
    magnetic_content = fields.Html(string="Magnetic content")