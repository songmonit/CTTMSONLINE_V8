from openerp.osv import osv, fields

class sale_order(osv.osv):
    _name = "sale.order"
    _inherit = ['sale.order', 'crm.tracking.mixin']
    _columns = {
        'categ_ids': fields.many2many('crm.case.categ', 'sale_order_category_rel', 'order_id', 'category_id', 'Tags', \
            domain="['|', ('section_id', '=', section_id), ('section_id', '=', False), ('object_id.model', '=', 'crm.lead')]", context="{'object_name': 'crm.lead'}")
    }
