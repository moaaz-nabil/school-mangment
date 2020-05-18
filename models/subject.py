from odoo import models, fields, api, _

class Subject(models.Model):
    _name = 'school.subject'
    _description = 'Subjects'
    _rec_name = 'name'

    name = fields.Char(string="Subject Name", required=True)
    code = fields.Char(string="Subject Code", readonly=True)
    total_degree = fields.Integer(required=True)
    pass_degree = fields.Integer(required=True)
    his_teacher = fields.Many2one('school.teacher',string="Subject Teacher", required=True)
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

    # Create Subject Sequence
    @api.model
    def create(self, vals):
        if vals.get('code', _('New')) == _('New'):
            vals['code'] = self.env['ir.sequence'].next_by_code('subject.sequence') or _('New')
        result = super(Subject, self).create(vals)
        return result 
