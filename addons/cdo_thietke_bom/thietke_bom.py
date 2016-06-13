# -*- coding: utf-8 -*-
##############################################################
#
#    Created on 31-12-2014
#
#    @author: Do Huy Cuong
#
##############################################################

from openerp.osv import fields
from openerp.osv import osv
from openerp.tools.translate import _
class thietke_bom(osv.osv):
    _name='thietke.bom'
    _description = u'Triển khai mẫu thiết kế'
    _columns={
              'bom_id':fields.many2one('mrp.bom','id',ondelete='set null'),
              'mautk_id':fields.many2one('cdo_thietke.mautk','id',ondelete='set null'),
    }
    _defaults={

               }
class cdo_thietke_mautk(osv.osv):
    _name='cdo_thietke.mautk'
    _inherit = 'cdo_thietke.mautk'
    _description = u'Thành phần nguyên vật liệu'
    _columns={
              'bom_id': fields.many2one('mrp.bom', u'BoM'),
    }