from odoo import models, fields


class ResPartner(models.Model):
    _inherit = "res.partner"

    journal_entry_ids = fields.One2many(
        "specialist.journal.entry",
        "partner_id",
        string="Specialist Journal"
    )
