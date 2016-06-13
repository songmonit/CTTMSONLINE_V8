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
    'name': 'Tạo BoM theo mẫu thiết kế',
    'version': '1.0',
    'category': 'Thiết Kế',
    'description': """
Module tạo BoM trong thiết kế.
=======================================================================================

Đây là module liệt kê chi tiết vật liệu đầu vào và thành phẩm khi hoàn thành .""",
    'author': 'Do Huy Cuong',
    'website': 'huycuongdo@gmail.com',
    'depends': ['cdo_thietke','mrp'],
    'data': [
        'thietke_bom_view.xml',
    ],
    #'qweb':['static/src/xml/image_khaosat.xml'],
    'demo': [],
    'test': [],
    'installable': True,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: