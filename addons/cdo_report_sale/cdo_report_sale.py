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
import openerp.addons.decimal_precision as dp
class cdoreport_sale(osv.osv):
    _name='cdoreport.sale'
	#_inherit = 'sale.report'
    _description = u'Biểu mẫu báo giá / đơn hàng'
	#_columns = {
        #'': fields.float('Discount', readonly=True, digits=dp.get_precision('Discount')),
	#	'price_subtotal_line': fields.float('Thành tiền', readonly=True),
    #}
	#def _select(self):
	#	res = super(DiscountSaleReport,self)._select()
    #   select_str = res+""",sum(l.product_uom_qty * cr.rate * l.price_unit) as price_subtotal_line"""
    #    return select_str	
	def docso(self, num=0):
        return "Một trăm"