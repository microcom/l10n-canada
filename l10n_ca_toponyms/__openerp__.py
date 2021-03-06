# -*- encoding: utf-8 -*-
##############################################################################
#
#    Odoo, Open Source Management Solution
#    Copyright (C) 2010 - 2014 Savoir-faire Linux
#    (<http://www.savoirfairelinux.com>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the Affero GNU General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the Affero GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': 'Canada - Provinces and Territories',
    'version': '9.0.0.0.0',
    'author': "Savoir-faire Linux,Odoo Community Association (OCA)",
    'website': 'http://www.savoirfairelinux.com',
    'category': 'Localisation/Canada',
    'license': 'AGPL-3',
    'description': """
Provinces and territories of Canada.
====================================

This module provides the list of provinces and territories of Canada.

Contributors
------------
* Virgil Dupras <virgil.dupras@savoirfairelinux.com>
* Maxime Chambreuil <maxime.chambreuil@savoirfairelinux.com>
* Sandy Carter <sandy.carter@savoirfairelinux.com>
""",
    'depends': ['base'],
    'data': [
        'l10n_ca_toponyms.xml',
    ],
    'installable': True,
}
