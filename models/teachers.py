from odoo import fields, models, api, _

class Teachers(models.Model):
    _name = 'school.teacher'
    _description = 'Teachers'
    _rec_name = 'name'

    name = fields.Char(string="Name", required=True)
    teacher_id = fields.Char(string="Teacher ID", readonly=True)
    phone = fields.Char()
    birth_date = fields.Date(string="Birth Date", required=True)
    teacher_picture = fields.Binary(string="Teacher Picture", attachment=True)
    nationality = fields.Many2one('res.country', required=True)
    email = fields.Char()
    gender = fields.Selection([
        ('male','Male'),
        ('famale','Famale')
    ], required=True)
    country_id = fields.Many2one('res.country')
    address_state = fields.Many2one('res.country.state')
    address_street = fields.Char()
    address_house_num = fields.Integer()
    user_id = fields.Many2one('res.users', 'User',readonly= True ,  ondelete="cascade")


    # Create Teacher Sequence
    @api.model
    def create(self, vals):
        if vals.get('teacher_id', _('New')) == _('New'):
            vals['teacher_id'] = self.env['ir.sequence'].next_by_code('teacher.sequence') or _('New')
        result = super(Teachers, self).create(vals)
        return result 

    # Create Teacher User
    @api.multi
    def create_teacher_user(self):
        user_group = self.env.ref("base.group_portal") or False
        users_res = self.env['res.users']
        for record in self:
            if not record.user_id:
                user_id = users_res.create({
                    'name': record.name,
                    'login': record.email,
                    'groups_id': user_group,
                    'image' :record.teacher_picture,
                    'is_student': True,
                    'tz': self._context.get('tz')
                })
                record.user_id = user_id
        