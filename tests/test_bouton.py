import unittest
from gpiozero import Button,Device
from gpiozero.pins.mock import MockFactory


Device.pin_factory = MockFactory()

class TestBouton(unittest.TestCase):
    def setUp(self):
        #Simulation bouton au GPIO13
        self.bouton = Button(13)

    #Verifie que le bouton est bien un objet Button
    def test_initialisation(self):
        self.assertIsInstance(self.bouton, Button)

    
        