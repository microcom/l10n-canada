# -*- encoding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2013 Savoir-faire Linux (<http://www.savoirfairelinux.com>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
	'name' : 'Quebec Enterprise Number (NEQ)',
	'version' : '1.1',
	"author" : "Savoir-faire Linux (mcassuto@savoirfairelinux.com)",
	"website" : "http://www.savoirfairelinux.com",
	'license': 'AGPL-3',
	'category' : 'Localisation/Canada',
	'depends' : ['base'],
	'description': """
Add the Quebec Enterprise Number (NEQ) to the partner form.
""",
	'auto_install': False,
	'installable': True,
	'data' : ['res_partner_attributes_add_NEQ_view.xml']
}


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: