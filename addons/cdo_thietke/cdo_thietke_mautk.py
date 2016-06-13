######################################################################
#
#    Created on 25-04-2014
#
#    @author: Do Huy Cuong
#
######################################################################

from openerp.osv import osv,fields
from openerp.tools.translate import _
from datetime import datetime
from openerp import tools

class cdo_thietke_mautk(osv.osv):
    _name='cdo_thietke.mautk'
    _inherit = ['mail.thread']
    _description = u'Mẫu thiết kế'
    _columns={
              'baomau_id':fields.many2one('cdo_thietke.baomau',u'Yêu cầu báo mẫu',ondelete='set null', select=True, track_visibility='onchange', help="Báo mẫu yêu cầu nào?.",
                                          write=['cdo_thietke.group_thietke_dp'],read=['cdo_thietke.group_thietke']),
              'designer_id':fields.many2one('res.users', u'Người thiết kế',track_visibility='onchange', help='Người phụ trách thiết kế.',
                                            write=['cdo_thietke.group_thietke_dp'],read=['cdo_thietke.group_thietke']),
              'chief_id':fields.many2one('res.users', u'Người giao', help='Người quản lý tiến độ mẫu thiết kế.',readonly=True),
              'manager_id':fields.many2one('res.users', u'Xét duyệt', help='Người chịu trách nhiệm về mẫu thiết kế.',readonly=True),
              'name':fields.char(u'Tên mẫu',size=250, track_visibility='onchange',
                                 write=['cdo_thietke.group_thietke_dp'],read=['cdo_thietke.group_thietke']),
              'path':fields.char(u'Vị trí lưu trữ files',size=250),
              'description':fields.text(u'Diễn giải',
                                        write=['cdo_thietke.group_thietke_dp'],read=['cdo_thietke.group_thietke']),
              'progress':fields.selection([(100,u'Xong(Báo mẫu)'),(90,'90%'),(80,'80%'),(70,'70%'),(60,'60%'),(50,'50%'),(40,'40%'),(30,'30%'),(20,'20%'),(10,'10%'),(1,u'Nhận việc')],u'Hoàn thành',track_visibility='onchange',
                                          write=['cdo_thietke.group_thietke_tk','cdo_thietke.group_thietke_dp'],read=['cdo_thietke.group_thietke']),
              'state':fields.selection([('open',u'Thiết kế'),('confirm',u'Duyệt mẫu'),('deploy',u'Triển khai'),('cancel',u'Hủy'),('done',u'Hoàn thành')],u'Trang thái',readonly=True,track_visibility='onchange',
                                        write=['cdo_thietke.group_thietke_dp'],read=['cdo_thietke.group_thietke']),
              'date_deadline':fields.datetime(u'Thời hạn hoàn thành', track_visibility='onchange',
                                              write=['cdo_thietke.group_thietke_dp'],read=['cdo_thietke.group_thietke']),
              'confirmed_date':fields.datetime(u'Ngày nhận', readonly=True),
              'date_done':fields.datetime(u'Ngày hoàn thành', readonly=True),
              'date':fields.datetime(u'Ngày Giao', readonly=True),
              'baomau_user_id': fields.related('baomau_id', 'user_id', type="many2one", relation="cdo_thietke.baomau", string=u"NV kinh doanh", readonly=True, required=True),
              'working_time':fields.integer(u'Thời gian đến hạn(Ngày)',readonly=True),
    }
    
    def _get_default_baomau_id(self,cr, uid, context=None):
        if context is None:
            context = {}
        baomau_obj = self.pool.get('cdo_thietke.baomau')
        active_id = context and context.get('active_id', False) or False
        if not active_id:
            return False

        design = baomau_obj.read(cr, uid, active_id, ['id'], context=context)
        return design['id'] if design['id'] else False
    
    def _get_default_baomau_name(self,cr, uid, context=None):
        if context is None:
            context = {}
        baomau_obj = self.pool.get('cdo_thietke.baomau')
        active_id = context and context.get('active_id', False) or False
        if not active_id:
            return False
        design = baomau_obj.read(cr, uid, active_id, ['name'], context=context)
        return design['name'] if design['name'] else False
    
    _defaults={
               'state': lambda *a: 'open',
               'baomau_id': _get_default_baomau_id,
               'chief_id':lambda s, cr, uid, c: uid,
               'name': _get_default_baomau_name,
               'date':fields.datetime.now,
               }
    
    def _check_dates(self, cr, uid, ids, context=None):
        for leave in self.read(cr, uid, ids, ['date_deadline', 'date'], context=context):
            if leave['date_deadline'] and leave['date']:
                if leave['date_deadline'] < leave['date']:
                    return False
        return True
    
    _constraints = [
        (_check_dates, u'Lỗi dữ liệu. Hãy kiểm tra lại giá trị ô Thời hạn hoàn thành', ['date_deadline', 'date'])
    ]
    
    def date_change(self,cr,uid,ids,val_deadline,context=None):
        if val_deadline==False: return True
        now =  datetime.now()
        workingtime=datetime.strptime(val_deadline, '%Y-%m-%d %H:%M:%S')- now
        workingtime_h=workingtime.days*24 + workingtime.seconds//3600
        if workingtime_h<1:
            raise osv.except_osv(u'Thay đổi thời hạn không được lưu!', u'CTTMS chỉ chấp nhận thay đổi từ 1h trở lên so với hiện tại.')
            return False
        else: return True
        
    def working_time_change(self,cr,uid,ids,context=None):
        now =  datetime.now()
        for leave in self.read(cr, uid, ids, ['progress','date_deadline'], context=context):
            if leave['progress']==100: return True
            workingtime=datetime.strptime(leave['date_deadline'], '%Y-%m-%d %H:%M:%S')- now #.strftime('%Y/%m/%d %H:%M:%S')
            workingtime1=workingtime.days #*24 + workingtime.seconds//3600
            self.write(cr, uid, ids, {'working_time': workingtime1}, context=context)
        return True
    def upd_working_time(self,cr,uid,context=None):
        mautk_obj= self.pool.get('cdo_thietke.mautk')
        ids=mautk_obj.search(cr, uid, [('progress','!=',100)])
        now =  datetime.now()
        for leave in self.read(cr, uid, ids, ['id','progress','date_deadline','state'], context=context):
            if (leave['date_deadline'] != 'open'):
                deadline=leave['date_deadline']
                workingtime=datetime.strptime(deadline,'%Y-%m-%d %H:%M:%S')-now
                self.write(cr, uid, leave['id'], {'working_time': workingtime.days}, context=context)
        print "Working time updated"
        return True
    def notice_by_email(self, cr, uid, ids, context=None):
        mail_to=''       
        mUsr = self.pool.get("res.users")
        for leave in self.read(cr, uid, ids, ['designer_id','name'], context=context):
            user = mUsr.browse(cr, uid, leave['designer_id'])
            mail_to=user.email
        mail_subject=u"Giao mẫu thiết kế"
        mail_from='auto@cttms.thanhtho.com'
        mail_body=u'THÔNG BÁO </br> Bạn nhận được yêu cầu thiết kế cho mẫu: '
        tools.email_send(mail_from, mail_to, mail_subject, mail_body)
        return True
    
    def mautk_open(self, cr, uid, ids, context=None):
        self.write(cr, uid, ids, { 'state' : 'open' })
        return True
    def mautk_confirmed(self, cr, uid, ids, context=None):
        for leave in self.read(cr, uid, ids, ['progress'], context=context):
            if leave['progress']<100: 
                raise osv.except_osv(u'Bạn không thể duyệt mẫu này!', u'Mẫu thiết kế chưa được hoàn thành.')
                return False
            else:
                self.write(cr, uid, ids, { 'state' : 'confirm' , 'manager_id':uid})
        return True
    def mautk_deploy(self, cr, uid, ids, context=None):
        self.write(cr, uid, ids, { 'state' : 'deploy' })
        return True
    def mautk_cancel(self, cr, uid, ids, context=None):
        self.write(cr, uid, ids, { 'state' : 'cancel' })
        return True
    def mautk_done(self, cr, uid, ids, context=None):
        self.write(cr, uid, ids, { 'state' : 'done' })
        return True
cdo_thietke_mautk()

class cdo_baomau_baomau(osv.osv):
    _name='cdo_thietke.baomau'
    _inherit='cdo_thietke.baomau'
    _columns={
              'mautk_ids': fields.one2many('cdo_thietke.mautk', 'baomau_id', u'Mẫu thiết kế'),
              }