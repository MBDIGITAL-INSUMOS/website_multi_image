from odoo import fields, osv, models, api
from odoo.tools.translate import _
import logging
_logger = logging.getLogger(__name__)
import urllib2
import pdb

class product_image(models.Model):
    _name = 'product.image'

    name = fields.Char('Name')
    description = fields.Text('Description')
    image = fields.Binary('Image')
    image_small = fields.Binary('Small Image')
    product_tmpl_id = fields.Many2one('product.template', 'Product')

product_image()

class product_product(models.Model):
    _inherit = 'product.product'

    images = fields.One2many(related='product_tmpl_id.images', string='Images', store=False)

product_product()

class product_template(models.Model):
    _inherit = 'product.template'

    images = fields.One2many('product.image', 'product_tmpl_id', string='Images')

product_template()
