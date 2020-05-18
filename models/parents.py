from odoo import models, fields, api, _

class Parents(models.Model):
    _name = 'school.parents'
    _description = 'Parents'
    _rec_name = 'name'
    _inherit = 'res.country'

    name = fields.Char(string="Name")
    parent_picture = fields.Binary(attachment=True)
    phone = fields.Char()
    his_children = fields.Many2many('school.student')
    national_id = fields.Char()
    nationality = fields.Many2one('res.country')
    parent_nationality = fields.Many2one('res.country')

    address_countery = fields.Many2one('res.country')
    address_state = fields.Many2one('res.country.state')
    address_street = fields.Char()
    address_house_num = fields.Integer()
    email = fields.Char()
    gender = fields.Selection([
        ('male','Male'),
        ('famale','Famale')
    ])
    user_id = fields.Many2one('res.users', 'User',readonly= True ,  ondelete="cascade")


    # Create Parent User
    @api.multi
    def create_parent_user(self):
        user_group = self.env.ref("base.group_portal") or False
        users_res = self.env['res.users']
        for record in self:
            if not record.user_id:
                user_id = users_res.create({
                    'name': record.name,
                    'login': record.email,
                    'groups_id': user_group,
                    'image' :record.parent_picture,
                    'is_student': True,
                    'tz': self._context.get('tz')
                })
                record.user_id = user_id
    

