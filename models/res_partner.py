from odoo import models, fields


class ResPartner(models.Model):
    _inherit = "res.partner"

    journal_entry_ids = fields.One2many(
        "specialist.journal.entry",
        "partner_id",
        string="Specialist Journal"
    )

    def print_journal_report(self):
        self.ensure_one()
        journal_entries = self.env['specialist.journal.entry'].search([('partner_id', '=', self.id)])
        return self.env.ref('journal_specialist.action_report_specialist_journal').report_action(journal_entries)
