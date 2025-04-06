import unittest
import base64

class Base16Test(unittest.TestCase):
    
    def test_base16_encode(self):
        b = bytes.fromhex('f9cdb9ec44d8d3c18d41cdf26ae6123c')
        encoded = base64.b16encode(b)
        self.assertEqual(b'F9CDB9EC44D8D3C18D41CDF26AE6123C', encoded)

    def test_base16_decode(self):
        s = b'F9CDB9EC44D8D3C18D41CDF26AE6123C'
        decoded = base64.b16decode(s)
        self.assertEqual('f9cdb9ec44d8d3c18d41cdf26ae6123c', decoded.hex())

if __name__ == '__main__':
    unittest.main()
