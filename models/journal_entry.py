from odoo import models, fields, api


class SpecialistJournalEntry(models.Model):
    _name = "specialist.journal.entry"
    _description = "Specialist Journal Entry"
    _order = "date desc"

    date = fields.Date(
        string="Date",
        default=fields.Date.context_today,
        required=True
    )
    user_id = fields.Many2one(
        "res.users",
        string="Specialist",
        default=lambda self: self.env.user,
        required=True
    )
    partner_id = fields.Many2one(
        "res.partner",
        string="Client",
        required=True,
        ondelete="cascade"
    )
    text = fields.Text(string="Journal Note", required=True)
