# -*- coding: utf-8 -*-
##############################################################
#
#    Created on 15-03-2014
#
#    @author: Do Huy Cuong
#
##############################################################
from openerp.osv import fields, osv

class cdo_thietke_baomau(osv.osv):
    _inherit = "cdo_thietke.baomau"

    _columns = {
                'multi_images': fields.text('Ảnh khảo sát'),
    }

cdo_thietke_baomau()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: