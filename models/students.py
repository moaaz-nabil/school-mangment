from odoo import fields, models, api, _ 

class Student(models.Model):
    _name = 'school.student'
    _description = 'Students'
    _rec_name = 'name_student'

    name_student = fields.Char(required=True)
    student_id = fields.Char(readonly=True)
    phone = fields.Char(required=True)
    parent = fields.Many2many('school.parents',required=True)
    gender = fields.Selection([
        ('male','Male'),
        ('famale','Famale')
    ],required=True)
    birth_date = fields.Date(required=True)
    student_pic = fields.Binary(attachment=True)
    student_nationality = fields.Many2one('res.country', required=True)
    national_id = fields.Char(required=True)
    email = fields.Char()
    country_id = fields.Many2one('res.country', required=True)
    address_state = fields.Many2one('res.country.state')
    address_street = fields.Char()
    address_house_num = fields.Integer()
    level = fields.Selection([
        ('prim1','Prim 1'),
        ('prim2','Prim 2'),
        ('prim3','Prim 3'),
        ('prim4','Prim 4'),
        ('prim5','Prim 5'),
        ('prim6','Prim 6'),
        ('sec1','Sec 1'),
        ('sec1','Sec 2'),
        ('sec1','Sec 3'),
    ])
    user_id = fields.Many2one('res.users', 'User',readonly= True ,  ondelete="cascade")
    degree = fields.One2many('school.degree', 'subject_rel')


    # Create Student Sequence
    @api.model
    def create(self, vals):
        if vals.get('student_id', _('New')) == _('New'):
            vals['student_id'] = self.env['ir.sequence'].next_by_code('student.sequence') or _('New')
        result = super(Student, self).create(vals)
        return result 

    # Create Student User
    @api.multi
    def create_student_user(self):
        user_group = self.env.ref("base.group_portal") or False
        users_res = self.env['res.users']
        for record in self:
            if not record.user_id:
                user_id = users_res.create({
                    'name': record.name_student,
                    'login': record.email,
                    'groups_id': user_group,
                    'image' :record.student_pic,
                    'is_student': True,
                    'tz': self._context.get('tz')
                })
                record.user_id = user_id
    