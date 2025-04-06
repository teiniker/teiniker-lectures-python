import unittest


class BytesTest(unittest.TestCase):

    def test_string_types(self):
        s1 = 'message'
        s2 = b'message'
        self.assertTrue(type(s1) is str)
        self.assertTrue(type(s2) is bytes)

    def test_constructor(self):
        msg = "message"
        b = bytes(msg, 'utf-8')
        self.assertTrue(type(b is bytes))
        self.assertEqual(b'message', b)

    def test_encode(self):
        msg = "message"
        b = "message".encode('utf-8')
        self.assertTrue(type(b is bytes))
        self.assertEqual(b'message', b)
        
    def test_fromhex(self):
        hex_str = 'f9cdb9ec44d8d3c18d41cdf26ae6123c'
        b = bytes.fromhex(hex_str)
        self.assertTrue(type(b is bytes))
        self.assertEqual(b'\xf9\xcd\xb9\xecD\xd8\xd3\xc1\x8dA\xcd\xf2j\xe6\x12<', b)
        
    def test_to_hex(self):
        b = b'\xf9\xcd\xb9\xecD\xd8\xd3\xc1\x8dA\xcd\xf2j\xe6\x12<'
        hex_str = b.hex()
        self.assertTrue(type(hex_str is str))
        self.assertEqual('f9cdb9ec44d8d3c18d41cdf26ae6123c', hex_str)

    def test_bytes_to_list(self):
        b = b'\xf9\xcd\xb9\xecD\xd8\xd3\xc1\x8dA\xcd\xf2j\xe6\x12<'
        l = list(b)
        self.assertTrue(type(l is list))
        self.assertEqual([249, 205, 185, 236, 68, 216, 211, 193, 141, 65, 205, 242, 106, 230, 18, 60], l)


if __name__ == '__main__':
    unittest.main()
