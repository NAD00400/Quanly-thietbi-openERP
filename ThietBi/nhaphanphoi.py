# -*- coding: utf-8 -*-
from openerp.osv import fields, osv

class NhaPhanPhoi(osv.osv):
    _name = 'nhaphanphoi.nhaphanphoi'
    _columns = {
        'name': fields.char('Tên nhà phân phối', required=True),
        'tax_code': fields.char('Mã số thuế', size=20, required=True),
        'address': fields.text('Địa chỉ'),
        'phone': fields.char('Số điện thoại'),
        'email': fields.char('Email'),
        'contact_person': fields.char('Người liên hệ chính'),
        'device_ids': fields.one2many(
            'device.device',  # Model đích
            'distributor_id',  # Trường liên kết trong model Device
            string='Danh sách thiết bị'
        ),
    }

    _sql_constraints = [
        ('tax_code_unique', 'unique(tax_code)', 'Ma so thue khong duoc trung!')  # Thông báo lỗi không dấu
    ]

NhaPhanPhoi()