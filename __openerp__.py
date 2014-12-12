# -*- coding: utf-8 -*-
{
    "name" : "CRM - Proposals",
    "summary":"""
        Create Proposals associated with an Opportunity
    """,
    "description" : """
    This module adds Proposals to Opportunities, where the final Proposal gets converted to a Quote, and from a quote to a Sales Order.
    """,
    "author" : "Transformix Engineering Inc.", 
    "website" : "http://www.Transformix.com",
    "depends" : ['base','crm', 'crm_eto'],
    "category" : "Customer Relationship Management",
    "version" : "0.1",
    "sequence": 16,
    #"init" : [],
    "demo" : [],
    #"data" : [],
    "data" : ["crm_proposal_view.xml",],    
    'test': [],
    #'installable': True,   
    #'complexity': "easy",
    #'active': False,
}