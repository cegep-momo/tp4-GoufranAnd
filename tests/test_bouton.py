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
 
   
    def test_bouton_enfonce(self):
        #Simule l'enfoncement du bouton
        self.bouton.pin.drive_low()
        self.assertTrue(self.bouton.is_pressed)
 
        #Simule le relachement du bouton
        self.bouton.pin.drive_high()
        self.assertFalse(self.bouton.is_pressed)
 