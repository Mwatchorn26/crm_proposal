# -*- coding: utf-8 -*-
from openerp.osv import fields, osv
from openerp import fields, models


class crm_opportunity_proposal(models.Model):
    """This is the basis of a proposal.
    
    Proposals are part of an opportunity. (Hence the many2one relationship)"""
    _name        = "crm.lead.proposal"
    _description = "Proposal"
    _inherit = ['mail.thread', 'ir.needaction_mixin']
    
    def _get_next_proposal_number(self):
        opportunity_id = self.crm.lead.browse(self._context.get('company_id'))        
        proposal_ids = self.env('crm.lead').search(domain=[('opportunity_id','=',opportunity_id)], limit=1, order='proposal_number DESC')
        if not proposal_ids:
            return 1
        return proposal_ids[0]+1
        
    name = fields.Char('Proposal Name', size=128, required=True, help="")
    active = fields.Boolean('Active', required=False, default=True)
    probability = fields.Float('Success Rate (%)',group_operator="avg", digits=(3,2), default=0.5)
    planned_revenue = fields.Float('Expected Revenue', track_visibility='always', required=True)
    proposal_number =fields.Integer('Proposal Number', compute = '_get_next_proposal_number', help="Many iterations of proposals may be submitted before winning the job. This tracks each proposal.")
    proposal_date = fields.Date(string='Proposal Date', select=True, default=fields.date.context_today, help="Date when proposal is created.")
    opportunity_id = fields.Many2one('crm.lead', 'Opportunity', domain=[('type', '=', 'opportunity'),], help='Opportunity to which this proposal belongs')
    #project_code:fields.Related('opportunity_id','project_code',type='char',relation='crm.lead.project_code', string='Project Code', readonly=True),
    #project_name:fields.Related('opportunity_id','project_name',tyep='char',relation='crm.lead.project_name', string='Project Name', readonly=True),
    #'proposal_number':fields.function(_get_next_proposal_number, string='Proposal Number', type='integer', method=True, store=True, help="Many iterations of proposals may be submitted before winning the job. This tracks each proposal ."),
    #'project_code':fields.char('Project Code', size=6, readonly=True, help="Something like 'ABC002'"),
    #'project_name':fields.char('Project Name', size=128, readonly=True, help="Project code name like 'Sirena'"),
    #'stage_id': fields.many2one('crm.case.stage', 'Stage', track_visibility='onchange',
    #          domain="[ ('fold', '=', False), ('type', '=', type)]"),
    #'state': fields.related('stage_id', 'state', type="selection", store=True,
    #  selection=[ ('draft','Draft'), ('sent','Sent'), ('accepted','Accepted'), ('rejected','Rejected'), ], string="Status", readonly=True,
    #  help='The Status is set to \'Draft\', when a proposal is created. If the proposal has been submitted to the client the Status is set to \'Sent\'. When a response has been received from the prospective client, the Status is set to \'Accepted\' or \'Rejected\'.'),              
    #_defaults = {
    #             'opportunity_id': lambda self, cr, uid, context: self.pool.get('opportunity_id'),
    #             #'proposal_number': lambda self, cr, uid, context: self.pool.get('ir.sequence').get(cr, uid, 'opportunity_id'),
    #          }
crm_opportunity_proposal()


class crm_opportuntiy_proposal_extras(models.Model):
    """These are the extras that an Opportunity may need when it deals with Proposals"""
    _name    = 'crm.lead'
    _inherit = 'crm.lead'
    proposal_id = fields.Many2one('crm.lead.proposal', 'Proposal', domain=[])
    proposal_due_date = fields.Date('Proposal Due Date', select=True, help="Date when proposal is due.")
    animation_due_date = fields.Date('Animation Due Date', select=True, help="Date when mechanical animation is due.")
    concept_due_date = fields.Date('Concept Due Date', select=True, help="Date when concept is due.")
    decision = fields.Selection([('Q1','Q1'),('Q2','Q2'),('Q3','Q3'),('Q4','Q4'),('budgetary','Budgetary'),('reference','For Reference')],'Decision Due')
    #'decision_id': fields.many2one('crm.lead.decision', 'Decision', domain=[]),
    #'quoted':fields.char('Quoted', size=16, required=False, help="Date or 'Concept Rqd'"),
    delivery = fields.Date('Delivery Date', select=True, help="Date when machine is to be delivered to customer.")
    summary_notes = fields.Text('Summary Notes')

crm_opportuntiy_proposal_extras()


#class crm_opportunity_Decision(osv.Model):
#    _name = 'crm.lead.decision'
#    _columns={
#              'decision':fields.char('Decision', size=32, required=False, help="Something like '15-Q3' for '3rd Quarter of 2015'"),
#              }
#crm_opportunity_Decision()

#class crm_opportunity_extras(osv.Model):
#    _name    = 'crm.lead'
#    _inherit = 'crm.lead'
#    _columns={
#              'proposal_due_date': fields.date('Proposal Due Date', select=True, help="Date when proposal is due."),
#              'animation_due_date': fields.date('Animation Due Date', select=True, help="Date when mechanical animation is due."),
#              'concept_due_date': fields.date('Concept Due Date', select=True, help="Date when concept is due."),
#              'decision': fields.selection([('Q1','Q1'),('Q2','Q2'),('Q3','Q3'),('Q4','Q4'),('budgetary','Budgetary'),('reference','For Reference')],'Decision Due'),
#              #'decision_id': fields.many2one('crm.lead.decision', 'Decision', domain=[]),
#              #'quoted':fields.char('Quoted', size=16, required=False, help="Date or 'Concept Rqd'"),
#              'delivery': fields.date('Delivery Date', select=True, help="Date when machine is to be delivered to customer."),
#              'summary_notes': fields.text('Summary Notes'),
#              }
#crm_opportunity_extras()