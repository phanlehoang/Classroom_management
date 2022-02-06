# -*- coding: utf-8 -*-
from odoo import fields, models


class Khoa(models.Model):
    _name = 'khoa'
    _description = 'Danh sách giảng viên'
    name = fields.Char('Tên khoa', required=True)
    code_department = fields.Char('Mã khoa', size=8, required=True)
    _sql_constraints = [
        ('unique_classroom_code', 'unique(code_department)', 'Code should be unique per department!'),
        ('unique_classroom_name', 'unique(name)', 'Name should be unique per department!')]
