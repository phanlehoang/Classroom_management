# -*- coding: utf-8 -*-

from odoo import fields, models, api


class Giangduong(models.Model):
    _name = 'giang.duong'
    _description = 'Danh sách giảng đường'
    name = fields.Char('Giảng Đường', required=True)
    code_classroom = fields.Char('Mã giảng đường', size=5, required=True)
    type_classroom = fields.Selection([("Chất lượng cao", "Chất lượng cao"), ("Thường", "Thường")],
                                      string='Loại Giảng đường', required=True)
    type_class = fields.Selection([("LT", "Lý thuyết"), ("TH", "Thực hành")], string='Tiết học', required=True)
    classroom = fields.Selection(
        [("Phòng học", "Phòng học"), ("Hội trường", "Hội trường"), ("Phòng thí nghiệm", "Phòng thí nghiệm"),
         ("Phòng máy", "Phòng máy")], string='Phòng', required=True)
    capacity = fields.Integer(string='Số ghế', required=True)
    activate = fields.Selection(
        [("Đang sử dụng", "Đang sử dụng"), ("Sẵn sàng", "Sẵn sàng"), ("Không thể sử dụng", "Không thể sử dụng")],
        string='Trạng thái', required=True)
    start = fields.Datetime("Sử dụng từ")
    lecturer = fields.Many2one('giang.vien', string='Giảng viên')
    end = fields.Datetime("Đến")
    _sql_constraints = [
        ('unique_classroom_code', 'unique(code_classroom)',
         'Mã giảng đường should be unique per classroom!'),('unique_classroom_lecturer', 'unique(lecturer)',
                                                           'Tên giảng viên sử dụng should be unique per classroom!')]

    @api.onchange('activate')
    def onchange_activate(self):
        if self.activate == "Sẵn sàng" or self.activate == "Không thể sử dụng":
            self.lecturer = None
            self.start = None
            self.end = None

    @api.onchange('lecturer')
    def onchange_name(self):
        if (self.lecturer != None):
            self.activate = "Đang sử dụng"

    @api.onchange('start', 'end')
    def onchange_end(self):
        if self.end != None:
            if str(self.end) < str(self.start):
                self.end = self.start

    @api.onchange('code_classroom')
    def onchange_name(self):
        if (self.code_classroom != False):
            self.name = "Giảng đường "
            self.name = self.name + str(self.code_classroom)
