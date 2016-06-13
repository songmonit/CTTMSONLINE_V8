# -*- coding: utf-8 -*-
##############################################################
#
#    Created on 15-03-2014
#
#    @author: Do Huy Cuong
#
##############################################################

from openerp.osv import osv,fields
class cdo_thietke_baomau(osv.osv):
    _name='cdo_thietke.baomau'
    _inherit = ['mail.thread']
    _description = u'Báo mẫu'
    _columns={
              'partner_id':fields.many2one('res.partner', u'Khách hàng', track_visibility='onchange', select=True, help="Báo mẫu cho khách hàng nào?."),
              'user_id':fields.many2one('res.users', u'Người yêu cầu', help='Nhân viên phụ trách báo mẫu cho khách hàng.', track_visibility='onchange'),
              'designer_id':fields.many2one('res.users', u'NV thiết kế', help='Nhân viên phụ trách thiết kế chính.', track_visibility='onchange'),
              'name': fields.char(u'Tên', size=200,required=True, translate=True, track_visibility='onchange'),
              'date_deadline_baomau': fields.datetime(u'Thời hạn báo mẫu', track_visibility='onchange'),
              'date_deadline_baogia': fields.datetime(u'Thời hạn báo giá', track_visibility='onchange'),
              'date_deadline':fields.datetime(u'Ngày lắp đặt', track_visibility='onchange'),
              'content':fields.text(u'Nội dung yêu cầu về sản phẩm', track_visibility='onchange'),
              'description': fields.text(u'Mô tả chi tiết đa đạc và địa điểm lắp đặt', track_visibility='onchange'),
              'Note': fields.text(u'Ghi chú', track_visibility='onchange'),
              'state':fields.selection([('new',u'Mới'),('price',u'Báo giá thiết kế'),('show',u'Báo mẫu'),('close',u'Đóng')],u'Trạng thái',readonly=True, track_visibility='onchange'),
              'create_date':fields.datetime('Ngày tạo', readonly=True),
              'path': fields.char(u'Thư mục lưu trữ', size=200, track_visibility='onchange'),
    }
    _defaults={
               'state': lambda *a: 'new',
               'user_id':lambda s, cr, uid, c: uid,
               }
    
    def baomau_close(self, cr, uid, ids, context=None):
        return self.write(cr, uid, ids, {'state': 'close'}, context=context)
    '''
    def baomau_new(self, cr, uid, ids, context=None):
        return self.write(cr, uid, ids, {'state': 'new'}, context=context)
    
    def baomau_price(self, cr, uid, ids, context={}):
        return self.write(cr, uid, ids, {'state': 'price'}, context=context)

    def baomau_confirmed(self, cr, uid, ids, context={}):
        return self.write(cr, uid, ids, {'state': 'confirmed'}, context=context)
    
    def baomau_cancel(self, cr, uid, ids, context={}):
        return self.write(cr, uid, ids, {'state': 'cancel'}, context=context)
'''