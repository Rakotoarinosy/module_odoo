# -*- coding: utf-8 -*-

from odoo import exceptions, models, fields, api


class ConfirmationFacture(models.Model):
    _inherit = 'account.move'

    def confirmation_facture(self):
        for facture in self:
            if facture.state == 'posted': # type: ignore
                nom = facture.env.user.name
                permier_lettre = nom[0].upper()
                
                if permier_lettre.isalpha():
                    valeur_numerique_lettre = ord(permier_lettre) - ord('A') +1
                    if valeur_numerique_lettre % 2 != 0:
                        raise exceptions.UserError(
                            "Vous ne pouvez pas confirmer une facture"
                        )
        
    
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

