# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ResPartner(models.Model):
    _inherit = 'res.partner'

    # 定义扩展字段
    # 名称


class ResCompany(models.Model):
    _inherit = 'res.company'

    en_name = fields.Char(string='英文名称')
    explain = fields.Char(string='授权说明')


class MaintainOrder(models.Model):
    _name = 'maintain.order'
    _description = 'maintain order'
    _rec_name = 'name'

    # 表单主要信息
    name = fields.Char(string='账单号')
    license_plate = fields.Char(string='车牌号')
    order_no = fields.Char(string='订单号')
    print_date = fields.Datetime(string='打印日期')
    repair_date = fields.Datetime(string='修理日期')
    identifier_fin = fields.Char(string='车辆识别号', help='FIN')
    fir_reg_time = fields.Datetime(string='首次登记日期')
    notice_time = fields.Datetime(string='通知日期')
    repair_adviser = fields.Char(string='维修顾问')
    identifier_vin = fields.Char(string='车辆识别号', help='VIN')
    next_maintain_date = fields.Datetime(string='下次建议保养日期')
    old_recover = fields.Char(string='旧件回收')
    engine_num = fields.Char(string='发动机号')
    car_mode = fields.Char(string='车款')
    enter_time = fields.Datetime(string='进厂时间')

    # 表单次要信息
    subtotal_price = fields.Float(string='小计')
    work_hour = fields.Float(string='工时')
    car_parts = fields.Float(string='零件')
    order_other = fields.Float(string='其他')
    service_set = fields.Float(string='套餐')
    total_price = fields.Float(string='总计')
    service_note = fields.Text(string='服务备注')

    maintain_order_line = fields.One2many(comodel_name='maintain.order_line', inverse_name='maintain_order_id')


LINE_TYPE = [('t', '工时')]


class MaintainOrderLine(models.Model):
    _name = 'maintain.order_line'
    _description = 'maintain order line'
    _rec_name = 'code'

    maintain_order_id = fields.Many2one(comodel_name='maintain.order')

    seq = fields.Integer(string='序号')
    code = fields.Char(string='代码')
    line_type = fields.Selection(string='类型', selection=LINE_TYPE)
    description = fields.Char(string='说明')
    line_flag = fields.Char(string='标识')
    partner_type_no = fields.Char(string='客户类型编号')
    price = fields.Float(string='单价', help='单位(元)')
    unit = fields.Float(string='数量')
    discount_percent = fields.Float(string='折扣率')
    total_price = fields.Float(string='金额', help='单位(元)')
