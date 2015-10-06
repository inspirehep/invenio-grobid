# -*- coding: utf-8 -*-
#
# This file is part of Invenio.
# Copyright (C) 2015 CERN.
#
# Invenio is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation; either version 2 of the
# License, or (at your option) any later version.
#
# Invenio is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Invenio; if not, write to the Free Software Foundation, Inc.,
# 59 Temple Place, Suite 330, Boston, MA 02111-1307, USA.

import os
import pkg_resources

from invenio_grobid.mapping import tei_to_dict

from invenio.testsuite import InvenioTestCase


class TestMapping(InvenioTestCase):

    """Test invenio_grobid's TEI to dict mapping."""

    def setup_class(self):
        """Load a TEI and the expected dict."""
        self.dict = {
            'title': 'The Need to Fairly Confront Spin-1 for the New Higgs-like Particle',
            'authors': [
                {
                    'name': 'John P. Ralston',
                    'affiliations': [{'value': 'University of Kansas'}]
                }
            ],
            'abstract': 'Spin-1 was ruled out early in LHC reports of a new particle with mass near 125 GeV. Actually the spin-1 possibility was dismissed on false premises, and remains open. Model-independent classification based on Lorentz invariance permits nearly two dozen independent amplitudes for spin-1 to two vector particles, of which two remain with on-shell photons. The Landau-Yang theorems are inadequate to eliminate spin-1. Theoretical prejudice to close the gaps is unreliable, and a fair consideration based on experiment is needed. A spin-1 field can produce the resonance structure observed in invariant mass distributions, and also produce the same angular distribution of photons and ZZ decays as spin-0. However spin-0 cannot produce the variety of distributions made by spin-1. The Higgs-like pattern of decay also cannot rule out spin-1 without more analysis. Upcoming data will add information, which should be analyzed giving spin-1 full and unbiased consideration that has not appeared before.',
            'references': [
                {
                    'authors': [
                        {
                            'name': 'G Aad',
                            'affiliations': []
                        }
                    ],
                    'ref_title': None,
                    'journal_pubnote': {
                        'journal_issue': '1',
                        'journal_title': 'ATLAS Collaboration] Phys. Lett. B',
                        'journal_volume': '716',
                        'page_range': '',
                        'year': '2012'
                    }
                },
                {
                    'authors': [
                        {
                            'name': 'S Chatrchyan',
                            'affiliations': []
                        }
                    ],
                    'ref_title': None,
                    'journal_pubnote': {
                        'journal_issue': '30',
                        'journal_title': 'CMS Collaboration] Phys. Lett. B',
                        'journal_volume': '716',
                        'page_range': '',
                        'year': '2012'
                    }
                },
                {
                    'authors': [
                        {
                            'name': 'T Aaltonen',
                            'affiliations': []
                        }
                    ],
                    'ref_title': None,
                    'journal_pubnote': {
                        'journal_title': 'CDF and D0 Collaborations Phys. Rev. Lett',
                        'journal_volume': '109',
                        'page_range': '',
                        'year': '2012'
                    }
                },
                {
                    'authors': [
                        {
                            'name': 'S Weinberg',
                            'affiliations': []
                        },
                        {
                            'name': 'L Susskind Chatrchyan',
                            'affiliations': []
                        }
                    ],
                    'ref_title': 'For recent limits see S',
                    'journal_pubnote': {
                        'journal_issue': '109',
                        'journal_title': 'Phys. Rev. D Phys. Rev. DCMS Collaboration] Phys. Rev. Lett',
                        'journal_volume': '19',
                        'page_range': '1277-141801',
                        'year': '1979'
                    }
                },
                {
                    'authors': [],
                    'ref_title': None,
                    'journal_pubnote': {
                        'journal_title': 'General tests of symmetries will depend on a particular theory and its Ward identities',
                        'page_range': ''
                    }
                },
                {
                    'authors': [
                        {
                            'name': 'E C G. Stueckelberg',
                            'affiliations': []
                        },
                        {
                            'name': 'V I. Helv',
                            'affiliations': []
                        },
                        {
                            'name': 'I V. Ogievetskii',
                            'affiliations': []
                        },
                        {
                            'name': 'T Polubarinov',
                            'affiliations': []
                        },
                        {
                            'name': 'T Kunimasa',
                            'affiliations': []
                        },
                        {
                            'name': 'A A. Goto',
                            'affiliations': []
                        },
                        {
                            'name': 'Slavnov',
                            'affiliations': []
                        },
                        {
                            'name': 'Phys',
                            'affiliations': []
                        },
                        {
                            'name': 'Lett',
                            'affiliations': []
                        }
                    ],
                    'ref_title': None,
                    'journal_pubnote': {
                        'journal_issue': '21',
                        'journal_title': 'Phys. Acta. Prog. Theor. Phys. Veltman, Nucl.Phys. Phys. Rev. Lett',
                        'journal_volume': '11',
                        'page_range': '452-2610',
                        'year': '1938'
                    }
                },
                {
                    'authors': [
                        {
                            'name': 'S V. Lett',
                            'affiliations': []
                        },
                        {
                            'name': 'D G C. Kuzmin',
                            'affiliations': []
                        },
                        {
                            'name': 'Mckeon',
                            'affiliations': []
                        },
                        {
                            'name': 'Mod',
                            'affiliations': []
                        }
                    ],
                    'ref_title': None,
                    'journal_pubnote': {
                        'journal_issue': '33',
                        'journal_title': 'Phys. Lett.A Phys. Lett. Burnel, Phys Rev',
                        'journal_volume': '58',
                        'page_range': '2981-2985',
                        'year': '1986'
                    }
                },
                {
                    'authors': [
                        {
                            'name': 'J C. Pati',
                            'affiliations': []
                        },
                        {
                            'name': 'A Salam',
                            'affiliations': []
                        },
                        {
                            'name': 'Phys Lett',
                            'affiliations': []
                        },
                        {
                            'name': 'P H. Frampton',
                            'affiliations': []
                        },
                        {
                            'name': 'S L. Glashow',
                            'affiliations': []
                        },
                        {
                            'name': 'M O. Wanninger',
                            'affiliations': []
                        },
                        {
                            'name': 'J H. Antunano',
                            'affiliations': []
                        },
                        {
                            'name': 'G Kuhn',
                            'affiliations': []
                        },
                        {
                            'name': 'H. Rodrigop',
                            'affiliations': []
                        },
                        {
                            'name': 'J Frampton',
                            'affiliations': []
                        },
                        {
                            'name': 'K Shu',
                            'affiliations': []
                        },
                        {
                            'name': 'Wang',
                            'affiliations': []
                        }
                    ],
                    'journal_pubnote': {
                        'journal_title': 'Marques Tavares and M. Schmaltz Gabrielli and M. Raidal',
                        'page_range': '014003-054008',
                        'year': '1975'
                    },
                    'ref_title': '[arXiv:0709.1652 [hep-ph'
                },
                {
                    'authors': [
                        {
                            'name': 'T Aaltonen',
                            'affiliations': []
                        }
                    ],
                    'ref_title': None,
                    'journal_pubnote': {
                        'journal_issue': '84',
                        'journal_title': 'Phys. Rev. DD0 Collaboration] Phys. Rev. D',
                        'journal_volume': '83',
                        'page_range': '112003-112005',
                        'year': '2011'
                    }
                },
                {
                    'authors': [
                        {
                            'name': 'L D. Landau',
                            'affiliations': []
                        }
                    ],
                    'ref_title': None,
                    'journal_pubnote': {
                        'journal_title': 'Dokl. Akad. Nauk Ser.Fiz',
                        'journal_volume': '60',
                        'page_range': '',
                        'year': '1948'
                    }
                },
                {
                    'authors': [
                        {
                            'name': 'C N. Yang',
                            'affiliations': []
                        }
                    ],
                    'ref_title': None,
                    'journal_pubnote': {
                        'journal_title': 'Phys. Rev',
                        'journal_volume': '77',
                        'page_range': '',
                        'year': '1950'
                    }
                },
                {
                    'authors': [
                        {
                            'name': 'S Y. Choi',
                            'affiliations': []
                        },
                        {
                            'name': 'D J. Miller',
                            'affiliations': []
                        },
                        {
                            'name': '2',
                            'affiliations': []
                        },
                        {
                            'name': 'M M. Muhlleitner',
                            'affiliations': []
                        },
                        {
                            'name': 'P M. Zerwas',
                            'affiliations': []
                        }
                    ],
                    'ref_title': None,
                    'journal_pubnote': {
                        'journal_issue': '101',
                        'journal_title': 'Phys. Lett. B Phys. Rev. Lett',
                        'journal_volume': '553',
                        'page_range': '',
                        'year': '2003'
                    }
                },
            ]
        }
        self.tei = pkg_resources.resource_string(
            'tests', os.path.join('fixtures', 'article.xml')
        )

    def test_tei_to_dict(self):
        """Convert TEI to the internal dict representation."""
        self.assertEqual(self.dict, tei_to_dict(self.tei))
