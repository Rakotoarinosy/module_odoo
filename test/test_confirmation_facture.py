from odoo.tests.common import TransactionCase
from odoo import exceptions

class TestConfirmationFacture(TransactionCase):

    def setUp(self):
        super(TestConfirmationFacture, self).setUp()
        
        # utilisateur dont le nom commence par une lettre impaire
        self.user_impair = self.env['res.users'].create({
            'name': 'Alice',  # 'A' est impair
            'login': 'alice',
            'email': 'alice@example.com',
        })

        # utilisateur dont le nom commence par une lettre paire
        self.user_paire = self.env['res.users'].create({
            'name': 'Bob',  # 'B' est pair
            'login': 'bob',
            'email': 'bob@example.com',
        })
    
        # facture dans l'état 'posted'
        self.facture = self.env['account.move'].create({
            'state': 'posted',
        })
        
    def test_confirmation_facture_utilisateur_impair(self):
        # Test pour vérifier que l'utilisateur avec une lettre impaire est bloqué
        # Change l'utilisateur actuel pour self.user_impair
        self.env.user = self.user_impair
        with self.assertRaises(exceptions.UserError): # type: ignore
            self.facture.confirmation_facture()

    def test_confirmation_facture_utilisateur_paire(self):
        # Test pour vérifier que l'utilisateur avec une lettre paire peut confirmer la facture
        # Change l'utilisateur actuel pour self.user_paire
        self.env.user = self.user_paire
        try:
            self.facture.confirmation_facture()
        except exceptions.UserError:
            self.fail("L'utilisateur avec un nom commençant par une lettre paire ne devrait pas être bloqué.")