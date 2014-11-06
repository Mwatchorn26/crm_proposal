# -*- coding: utf-8 -*-

{
    "name" : "CRM Proposal Module",
    "version" : "0.1",
    "author" : "Transformix Engineering Inc.",
    'complexity': "easy",
    "description" : """
    This module adds Proposals to Opportunities, where the final Proposal gets converted to a Quote, and from a quote to a Sales Order.
    """,
    "website" : "http://www.Transformix.com",
    "depends" : ['crm'],
    "category" : "CRM",
    "sequence": 16,
    "init_xml" : [],
    "demo_xml" : [],
    "update_xml" : ["crm_proposal_view.xml",],
    'test': [],
    'installable': True,
    'application': True,
    'active': False,
}