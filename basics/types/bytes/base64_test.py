import unittest
import base64

class Base64Test(unittest.TestCase):
        
    def test_base64_encode(self):
        b = bytes.fromhex('f9cdb9ec44d8d3c18d41cdf26ae6123c')
        encoded = base64.standard_b64encode(b)
        self.assertEqual(b'+c257ETY08GNQc3yauYSPA==', encoded)

    def test_base64_decode(self):
        s = b'+c257ETY08GNQc3yauYSPA=='
        decoded = base64.standard_b64decode(s)
        self.assertEqual('f9cdb9ec44d8d3c18d41cdf26ae6123c', decoded.hex())


    def test_base64_url_encode(self):
        b = bytes.fromhex('f9cdb9ec44d8d3c18d41cdf26ae6123c')       
        encoded = base64.urlsafe_b64encode(b)
        self.assertEqual(b'-c257ETY08GNQc3yauYSPA==', encoded)

    def test_base64_url_decode(self):
        s = b'-c257ETY08GNQc3yauYSPA=='
        decoded = base64.urlsafe_b64decode(s)        
        self.assertEqual('f9cdb9ec44d8d3c18d41cdf26ae6123c', decoded.hex())

if __name__ == '__main__':
    unittest.main()
