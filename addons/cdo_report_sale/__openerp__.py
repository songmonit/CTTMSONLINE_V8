# -*- coding: utf-8 -*-
##############################################################################
#
#    Biểu mẫu
#
#    Created on 13-03-2014
#    @author: Do Huy Cuong
#
##############################################################################


{
    'name': 'Biểu mẫu in báo giá / đơn hàng',
    'version': '1.0',
    'category': 'sale',
    'description': """
Mẫu in báo giá / Đơn hàng.
=======================================================================================

Module cung cấp biểu mẩu báo giá và đơn hàng .""",
    'author': 'Do Huy Cuong',
    'website': 'huycuongdo@gmail.com',
    'depends': ['base_setup','sale', 'report'],
    'data': [
		'cdo_report_sale.xml',
        'cdo_report_sale_view.xml',
    ],
    'demo': [],
    'test': [],
    'installable': True,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: