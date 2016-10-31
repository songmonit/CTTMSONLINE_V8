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


class design_make_sale(osv.osv_memory):
    """ Make sale  order for design """

    _name = "design.make.sale"
    _description = "Make sales"

    def _selectPartner(self, cr, uid, context=None):
        """
        This function gets default value for partner_id field.
        @param self: The object pointer
        @param cr: the current row, from the database cursor,
        @param uid: the current user’s ID for security checks,
        @param context: A standard dictionary for contextual values
        @return: default value of partner_id field.
        """
        if context is None:
            context = {}

        design_obj = self.pool.get('cdo_thietke.baomau')
        active_id = context and context.get('active_id', False) or False
        if not active_id:
            return False

        design = design_obj.read(cr, uid, active_id, ['partner_id'], context=context)
        return design['partner_id'][0] if design['partner_id'] else False

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
        return super(design_make_sale, self).view_init(cr, uid, fields_list, context=context)

    def makeOrder(self, cr, uid, ids, context=None):
        """
        This function  create Quotation on given case.
        @param self: The object pointer
        @param cr: the current row, from the database cursor,
        @param uid: the current user’s ID for security checks,
        @param ids: List of crm make sales' ids
        @param context: A standard dictionary for contextual values
        @return: Dictionary value of created sales order.
        """
        if context is None:
            context = {}
        context.pop('default_state', False)        
        
        case_obj = self.pool.get('crm.lead')
        design_obj = self.pool.get('cdo_thietke.baomau')
        sale_obj = self.pool.get('sale.order')
        partner_obj = self.pool.get('res.partner')
        data = context and context.get('active_ids', []) or []

        for make in self.browse(cr, uid, ids, context=context):
            partner = make.partner_id
            partner_addr = partner_obj.address_get(cr, uid, [partner.id],
                    ['default', 'invoice', 'delivery', 'contact'])
            pricelist = partner.property_product_pricelist.id
            fpos = partner.property_account_position and partner.property_account_position.id or False
            payment_term = partner.property_payment_term and partner.property_payment_term.id or False
            new_ids = []
            #for case in case_obj.browse(cr, uid, data, context=context):
            #    case_sectionid=case.section_id and case.section_id.id or False
            for design in design_obj.browse(cr, uid, data, context=context):
                if not partner and design.partner_id:
                    partner = design.partner_id
                    fpos = partner.property_account_position and partner.property_account_position.id or False
                    payment_term = partner.property_payment_term and partner.property_payment_term.id or False
                    partner_addr = partner_obj.address_get(cr, uid, [partner.id],
                            ['default', 'invoice', 'delivery', 'contact'])
                    pricelist = partner.property_product_pricelist.id
                if False in partner_addr.values():
                    raise osv.except_osv(_(u'Thiếu dữ liệu!'), _(u'Chưa có thông tin địa chỉ khách hàng.'))

                vals = {
                    'origin': _('Báo mẫu: %s') % (design.name),
                    #'section_id': case_sectionid,
                    #'categ_ids': [(6, 0, [categ_id.id for categ_id in case.categ_ids])],
                    'baomau_id': design.id,
                    'partner_id': partner.id,
                    'pricelist_id': pricelist,
                    'partner_invoice_id': partner_addr['invoice'],
                    'partner_shipping_id': partner_addr['delivery'],
                    'date_order': fields.date.context_today(self,cr,uid,context=context),
                    'fiscal_position': fpos,
                    'payment_term':payment_term,
                }
                if partner.id:
                    vals['user_id'] = partner.user_id and partner.user_id.id or uid
                new_id = sale_obj.create(cr, uid, vals, context=context)
                sale_order = sale_obj.browse(cr, uid, new_id, context=context)
                design_obj.write(cr, uid, [design.id], {'ref': 'sale.order,%s' % new_id})
                new_ids.append(new_id)
                message = _("Yêu cầu báo mẩu đã tạo báo giá thiết kế <em>%s</em>.") % (sale_order.name)
                design.message_post(body=message)
                #update design_obj.state=price
                design_obj.write(cr, uid, [design.id], {'state': 'price'})

            if not new_ids:
                return {'type': 'ir.actions.act_window_close'}
            if len(new_ids)<=1:
                value = {
                    'domain': str([('id', 'in', new_ids)]),
                    'view_type': 'form',
                    'view_mode': 'form',
                    'res_model': 'sale.order',
                    'view_id': False,
                    'type': 'ir.actions.act_window',
                    'name' : _('Báo giá'),
                    'res_id': new_ids and new_ids[0]
                }
            else:
                value = {
                    'domain': str([('id', 'in', new_ids)]),
                    'view_type': 'form',
                    'view_mode': 'tree,form',
                    'res_model': 'sale.order',
                    'view_id': False,
                    'type': 'ir.actions.act_window',
                    'name' : _('Báo giá'),
                    'res_id': new_ids
                }
            return value


    _columns = {
        'partner_id': fields.many2one('res.partner', u'Khách hàng', required=True, domain=[('customer','=',True)]),
        'baomau_id': fields.many2one('cdo_thietke.baomau', u'Yêu cầu báo mẫu'),
    }
    
    
    _defaults = {
        'partner_id': _selectPartner,
        'baomau_id': _get_default_design_id,
    }


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
