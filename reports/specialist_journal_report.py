from odoo import models, api

class SpecialistJournalReport(models.AbstractModel):
    _name = 'report.journal_specialist.report_specialist_journal'
    _description = 'Specialist Journal Report'

    @api.model
    def _get_report_values(self, docids, data=None):
        records = self.env['specialist.journal.entry'].browse(docids)
        return {
            'doc_ids': docids,
            'doc_model': 'specialist.journal.entry',
            'docs': records,
        }
