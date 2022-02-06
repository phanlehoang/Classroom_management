# -*- coding: utf-8 -*-
from odoo import fields, models, api


class Giangvien(models.Model):
    _name = 'giang.vien'
    _description = 'Danh sách giảng viên'
    name = fields.Char('Giảng viên')
    picture = fields.Binary('Ảnh')
    lecturer = fields.Char('Tên giảng viên', required=True)
    code = fields.Char('Mã giảng viên', size=8, required=True)
    title = fields.Selection(
        [("CN", "Cử nhân"), ("ThS", "Thạc sĩ"), ("TS", "Tiến sĩ"), ("PGS", "Phó Giáo Sư"), ("GS", "Giáo Sư")],
        string='Học hàm / Học vị')
    department = fields.Many2one('khoa', string='Khoa')
    _sql_constraints = [('unique_classroom_code', 'unique(code)', 'Code should be unique per lecturer!')]

    @api.onchange('lecturer', 'name', 'code', 'title')
    def onchange_name(self):
        if (self.code != False and self.title != False):
            self.name = None
            self.name = str(self.code) + " - " + str(self.title) + ". " + self.lecturer
