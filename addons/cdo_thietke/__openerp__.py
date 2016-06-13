# -*- coding: utf-8 -*-
##############################################################################
#
#    Module quan ly bao mau trong thiet ke
#
#    Created on 13-03-2014
#    @author: Do Huy Cuong
#
##############################################################################


{
    'name': 'Quản lý Thiết kế',
    'version': '1.0',
    'category': 'Thiết Kế',
    'description': """
Module Quản lý mẫu trong thiết kế.
=======================================================================================

Đây là module quản lý việc yêu cầu báo mẫu của khác hàng và việc thiết kế mẫu của nhân viên thiết kế .""",
    'author': 'Do Huy Cuong',
    'website': 'huycuongdo@gmail.com',
    'depends': ['mail','base','document'],
    'data': [
        'security/cdo_thietke_security.xml',
        'security/ir.model.access.csv',
        'views/cdo_thietke_view.xml',
        'views/cdo_thietke_menu.xml',
        'views/cdo_thietke_baomau_images_view.xml',
        'views/cdo_thietke_mautk_view.xml',
        'views/cdo_thietke_mautk_images_view.xml',
        'workflow/cdo_thietke_workflow.xml',
    ],
    #'qweb':['static/src/xml/image_khaosat.xml'],
    'demo': [],
    'test': [],
    'installable': True,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: