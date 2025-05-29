# -*- coding: utf-8 -*-
from openerp.osv import fields, osv
import re

class device(osv.osv):
    _name = 'device.device'
    def _get_status(self, cr, uid, ids, field_name, args, context=None):
        res = {}
        for record in self.browse(cr, uid, ids, context=context):
            res[record.id] = "Đang hoạt động" if record.active else "Đã ngưng hoạt động"
        return res
    _columns = {
        'device_code': fields.char('Mã thiết bị', size=10, required=True),
        'name': fields.char('Tên thiết bị', size=100, required=True),
        'date_joined': fields.date('Ngày nhập'),
        'storage_id': fields.many2one('storage.storage', string='Kho thiết bị', required=True),
        'active': fields.boolean('Hoạt động'),
        'position': fields.char('Vị trí'),
       
        'status': fields.function(
            _get_status, type='char', string='Trạng thái', store=True
        ),
        'sl':fields.integer('Số lượng'),
        'dg': fields.float('Đơn giá'),
        
        'distributor_id': fields.many2one(
            'nhaphanphoi.nhaphanphoi',  # Tên model Nhà phân phối
            string='Nhà phân phối',
            required=True  # Yêu cầu chọn nhà phân phối khi nhập thiết bị
        ),
        
    }
    _defaults = {
        'active': True
    }
    _sql_constraints = [
        ('device_code_unique', 'unique(device_code)', 'Mã thiết bị không được trùng lặp!')
    ]
    
    
device()
