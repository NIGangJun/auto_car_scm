# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


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

    @api.model
    def create(self, vals):
        """
        继承创建方法
        :param vals:
        :return:
        """
        if vals.get('name', _('New')) == _('New'):
            vals['name'] = self.env['ir.sequence'].next_by_code('maintain.order') or _('New')
        res = super(MaintainOrder, self).create(vals)
        return res

    # 表单主要信息
    name = fields.Char(string='账单号')

    def _compute_bill_count(self):
        """
        计算订单下账单生成的数量
        :return:
        """
        for line in self:
            line.bill_count = '1/1'

    bill_count = fields.Char(string='账单数量', compute='_compute_bill_count')

    @api.onchange('license_plate')
    def _onchange_license_plate(self):
        """
        改变车牌号，默认将小写转换为大写
        :return:
        """

    license_plate = fields.Char(string='车牌号')
    order_no = fields.Char(string='订单号')
    print_date = fields.Datetime(string='打印日期')
    repair_date = fields.Datetime(string='修理日期')
    identifier_fin = fields.Char(string='车辆识别号(FIN)')
    fir_reg_time = fields.Datetime(string='首次登记日期', default=fields.Datetime.now)
    notice_time = fields.Datetime(string='通知日期')
    repair_adviser = fields.Many2one(comodel_name='res.partner', string='维修顾问')
    identifier_vin = fields.Char(string='车辆识别号(VIN)')
    next_maintain_date = fields.Datetime(string='下次建议保养日期')
    old_recover = fields.Char(string='旧件回收')
    engine_num = fields.Char(string='发动机号')
    car_mode = fields.Char(string='车款')
    enter_time = fields.Datetime(string='进厂时间', default=fields.Datetime.now)

    # 表单次要信息
    # todo 这下面的字段下次需要修改为只读，否则页面看起来会很奇怪
    subtotal_price = fields.Float(string='小计', readonly=True)
    work_hour = fields.Float(string='工时', readonly=True)
    car_parts = fields.Float(string='零件', readonly=True)
    order_other = fields.Float(string='其他', readonly=True)
    service_set = fields.Float(string='套餐', readonly=True)
    total_price = fields.Float(string='总计', readonly=True)
    service_note = fields.Text(string='服务备注', readonly=True)

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
