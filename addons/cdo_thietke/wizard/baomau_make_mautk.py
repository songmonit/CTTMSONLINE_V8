# -*- coding: utf-8 -*-
##############################################################
#
#    Created on 05-06-2014
#
#    @author: Do Huy Cuong
#
##############################################################
from openerp.osv import fields, osv
from openerp.tools.translate import _

class baomau_make_mautk(osv.osv_memory):
    """ Make mautk for baomau """

    _name = "baomau.make.mautk"
    _description = u"Giao thiết kế"

    def _get_default_design_id(self,cr, uid, context=None):
        if context is None:
            context = {}

        design_obj = self.pool.get('cdo_thietke.baomau')
        design_id = context and context.get('id', False) or False
        active_id = context and context.get('active_id', False) or False
        if not active_id:
            return False

        design = design_obj.read(cr, uid, active_id, ['id'], context=context)
        return design['id'] if design['id'] else False

    def view_init(self, cr, uid, fields_list, context=None):
        return super(baomau_make_mautk, self).view_init(cr, uid, fields_list, context=context)

    def makeMauTK(self, cr, uid, ids, context=None):
        if context is None:
            context = {}
        #context.pop('default_state', False)
        baomau_obj = self.pool.get('cdo_thietke.baomau')
        mautk_obj = self.pool.get('cdo_thietke.mautk')
        partner_obj = self.pool.get('res.partner')
        data = context and context.get('active_ids', []) or []
		
        for make in self.browse(cr, uid, ids, context=context):
            designer = make.designer_id
            baomau = make.baomau_id
            new_ids = []
            #    case_sectionid=case.section_id and case.section_id.id or False
            #for baomau in baomau_obj.browse(cr, uid, data, context=context):
            #for designer in partner_obj.browse(cr, uid, data, context=context):
                #if not designer and baomau.designer:
                #    designer = baomau.designer
            vals = {
                'baomau_id': baomau.id,
                'designer_id': designer.id,
            }
            new_id = mautk_obj.create(cr, uid, vals, context=context)
            mautk = mautk_obj.browse(cr, uid, new_id, context=context)
            new_ids.append(new_id)
            message = _(u"Đã được giao thiết kế <em>%s</em>.") % (mautk.name)
            baomau.message_post(body=message,)
			#update design_obj.state=show(design)
            baomau_obj.write(cr, uid, [baomau.id], {'state': 'show'})

            if not new_ids:
                return {'type': 'ir.actions.act_window_close'}
            if len(new_ids)<=1:
                value = {
                    'domain': str([('id', 'in', new_ids)]),
                    'view_type': 'form',
                    'view_mode': 'form',
                    'res_model': 'cdo_thietke.mautk',
                    'view_id': False,
                    'type': 'ir.actions.act_window',
                    'name' : _(u'Giao thiết kế'),
                    'res_id': new_ids and new_ids[0]
                }
            else:
                value = {
                    'domain': str([('id', 'in', new_ids)]),
                    'view_type': 'form',
                    'view_mode': 'tree,form',
                    'res_model': 'cdo_thietke.mautk',
                    'view_id': False,
                    'type': 'ir.actions.act_window',
                    'name' : _(u'Giao thiết kế'),
                    'res_id': new_ids
                }
            return value


    _columns = {
        'designer_id': fields.many2one('res.users', u'Người thiết kế'),
        'baomau_id': fields.many2one('cdo_thietke.baomau', u'Yêu cầu thiết kế', required=True),
    }
    
    
    _defaults = {
        'baomau_id': _get_default_design_id,
    }


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
