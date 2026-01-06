from odoo import models, fields

class SpecialistJournalTemplate(models.Model):
    _name = "specialist.journal.template"
    _description = "Journal Entry Template"

    name = fields.Char(required=True)
    content = fields.Text(string="Template Text", required=True)
