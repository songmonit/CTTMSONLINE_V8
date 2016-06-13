######################################################################
#
#    Created on 10-04-2014
#
#    @author: Do Huy Cuong
#
######################################################################

from openerp.osv import osv,fields

class cdo_thietke_baomau_images(osv.osv):
		
	_name='cdo_thietke_baomau.images'
	_description = u'Hình ảnh khảo sát'
	_columns={
              'img_url':fields.char(u'Nơi lưu ảnh',size=250),
              'image':fields.binary(u"Hình ảnh",help="Click để tải và lưu ảnh", track_visibility='onchange'),
              'file_name':fields.char('File name',size=250, track_visibility='onchange'),
              'name': fields.char(u'Tiêu đề', size=200),
              'description':fields.text(u'Mô tả hình ảnh'),
              'baomau_id':fields.many2one('cdo_thietke.baomau','id',ondelete='set null'),
              'mautk_id':fields.many2one('cdo_thietke.mautk','id',ondelete='set null'),
              }
	_defaults={}
cdo_thietke_baomau_images()

class cdo_thietke_baomau(osv.osv):
	_name='cdo_thietke.baomau'
	_inherit='cdo_thietke.baomau'
	_columns={
              'image_ids': fields.one2many('cdo_thietke_baomau.images', 'baomau_id', u'Hình ảnh'),
              }
cdo_thietke_baomau()
