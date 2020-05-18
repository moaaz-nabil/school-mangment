from odoo import models, api, fields, _

class Degree(models.Model):
    _name = 'school.degree'
    _description = 'Degree'
    _rec_name = 'subject_name'

    subject_name = fields.Many2one('school.subject')
    teacher = fields.Many2one('school.teacher', related='subject_name.his_teacher')
    student = fields.Many2one('school.student')
    total_degre = fields.Integer(readonly= True, related= 'subject_name.total_degree')
    pass_degree = fields.Integer(readonly= True, related= 'subject_name.pass_degree')
    his_degree = fields.Integer(string="His Degree")
    f_s = fields.Selection([
        ('fail','Fail'),
        ('sucsess','Sucsess')
    ], compute = 'fail_pass', readonly= True)
    subject_rel = fields.Many2one('school.subject')
    user_id = fields.Many2one('res,user', related='student.user_id')
    # Fail/Pass Function
    def fail_pass(self):
        for rec in self:
            if rec.pass_degree > rec.his_degree :
                rec.f_s = 'fail'
            elif rec.pass_degree <= rec.his_degree :
                rec.f_s = 'sucsess'
