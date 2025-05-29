# -*- coding: utf-8 -*-
from openerp.osv import fields, osv

class storage(osv.osv):
    _name = 'storage.storage'
    def _get_status(self, cr, uid, ids, field_name, args, context=None):
        res = {}
        for record in self.browse(cr, uid, ids, context=context):
            res[record.id] = "Đang hoạt động" if record.active else "Ngưng hoạt động"
        return res
    _columns = {
        'code': fields.char('Mã kho', size=10, required=True),
        'name': fields.char('Tên kho', size=100, required=True),
        'active': fields.boolean('Hoạt động'),
        'create_date': fields.datetime('Ngày tạo'),
        'position': fields.char('Vị trí kho'),
        'manager': fields.char('Người quản lý'),
        'device_ids': fields.one2many('device.device', 'storage_id', string='Thiết bị'),
        'status': fields.function(
            _get_status, type='char', string='Trạng thái', store=True
        ),
    }
    _defaults = {
        'active': True
    }
    _sql_constraints = [
        ('storage_code_unique', 'unique(code)', 'Mã kho không được trùng lặp!')
    ]

storage()
