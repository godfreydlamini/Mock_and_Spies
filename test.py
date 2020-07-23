import smtplib,unittest
from unittest import TestCase
from unittest.mock import Mock
from send_inspiration import main
import logging
mock = Mock()

m = mock.Mock()
class Sending_email(unittest.TestCase):
    def setUp(self):
        self.emails = []
    def test_get_contacts(self,*args):
        for i in self.emails:
            self.assertTrue(i == main(),'Incorrect')
        s = 'godfrey godfrey.dlamini@umuzi.org'
        self.assertEqual(s.split(), ['godfrey','godfrey.dlamini@umuzi.org'])
        with self.assertRaises(TypeError):
            s.split(2)
            self.assertEqual(len(s.emails), 2)
            self.assertEqual(s.emails[0].frm, 'godfrey.dlamini@umuzi.org'
            self.assertEqual(s.emails[1].to, 'godfreydlamini596@gmail.com'
            self.assertEqual(s.emails[0].msg, "Get Inspired Daily"
            self.assertEqual(m.get_contacts) == False
            
    

    def tearDown(self):
        self.emails = None
if __name__ == '__main__':
    unittest.main()