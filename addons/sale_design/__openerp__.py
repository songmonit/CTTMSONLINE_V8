# -*- coding: utf-8 -*-
##############################################################
#
#    Created on 05-06-2014
#
#    @author: Do Huy Cuong
#
##############################################################
{
    'name': 'Báo giá thiết kế',
    'version': '1.0',
    'category': 'Hidden',
    'description': """
Module tạo liên kết báo giá cho mẫu thiết kế.
===========================================================================

Nhân viên kinh doanh nhận yêu cầu và lấy thông tin từ khách hàng -> Cty sẽ tiến hành báo giá.

    - Nếu KH đồng ý -> Tạo mẫu thiết kế
    """,
    'author': 'Do Huy Cuong',
    'website': 'mailto:huycuongdo@gmail.com',
    'images': [],
    'depends': ['sale','crm', 'cdo_thietke', 'web_kanban_gauge'],
    'data': [
        'wizard/design_make_sale_view.xml',
        'sale_design_view.xml',
        #'sale_design_data.xml',
        'process/sale_design_process.xml',
        'security/sale_design_security.xml',
        'security/ir.model.access.csv',
        #'report/sale_report_view.xml',
    ],
    'js': [
        #'static/src/js/sale_crm.js',
    ],
    #'demo': ['sale_crm_demo.xml'],
    #'test': ['test/sale_crm.yml'],
    'installable': True,
    'auto_install': False,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
