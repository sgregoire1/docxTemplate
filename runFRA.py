# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from docxtpl import DocxTemplate
#from docx2pdf import doc2pdf

doc = DocxTemplate("./template/cv_fra.docx")
context = { 'NAME' : "Your Name",
            'JOB_NAME' : "Consultant Developpeur",
            'address':[ "Street line", "City, ST 10003"],
            'phone': "T 000 00 0 0000",
            'email' : "unknown@gmail.com",
            'profile' : "Aliquid albucius temporibus vis in. Mel in nisl inimicus, aeque intellegam disve bit theophrastus et eam. In tempor nostro adversarium nam. His ea alienumancillae, noster laoreet insolens cum id. Mazim tempor everti usu ei, tollit enique in his.",
            'skills' :["DEVISIVE THINKER",
                       "COLLABORATIVE",
                       "DRIVEN TO DELIVER",
                       "ROLE MODEL",
                       "DISCRETE AND ETHICAL"
                       ],
            'educations' :[ {'diploma' : "Master's degree in Information Technology",
                            'year' : "2001-2004",
                            'university' :"Conservatoire National des Arts et Metiers",
                            'city': "Evry, France"
                            }
                           , 
                            {'diploma' : "Two-year university degree in technology",
                            'year' : "1998-2000",
                            'university' :"Lycée R. Doisneau",
                            'city': "Corbeil-Essonnes, France"
                            }
                         ],
            'jobs' : [
            {'head': { 'date' : "2018-2020",
                      'jobName' :"JOB TITLE",
                      'compagny': "COMPANY NAME",
                      'city': "City",
                      'state': 'State'
                    },
            'body' : [{ 'title' : "Résponsabilités",
                     'value' : "Ut enim ad minim veniam, quis nostrud exerc. Irure dolor in reprehend incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi.",
                     'bulets' :[]
                    },
                    { 'title':"Réalisations",
                      'value' :"",
                      'bulets' :["Ut en im ad minim veniam, quis nostrud exerc",
                                 "Exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat",
                                 "Ut enim ad minim veniam, quis nostrud exerc"
                                ]
                    }]
            },
            {'head': { 'date' : "2005-2017",
                      'jobName' :"JOB TITLE",
                      'compagny': "COMPANY NAME",
                      'city': "City",
                      'state': 'State'
                    },
            'body' : [{ 'title' : "Résponsabilités",
                     'value' : "Ut enim ad minim veniam, quis nostrud exerc. Irure dolor in reprehend incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi.",
                     'bulets' :[]
                    },
                    { 'title': "Réalisations",
                      'value' :"",
                      'bulets' :["Ut en im ad minim veniam, quis nostrud exerc",
                                 "Exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat",
                                 "Ut enim ad minim veniam, quis nostrud exerc"
                                ]
                    }]
            }
            ]
            }
doc.render(context)
doc.save("./output/generated_fra.docx")

#doc2pdf("./output/generated_doc.docx","./output/generated_doc.pdf")
