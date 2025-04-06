import unittest


class ByteArrayTest(unittest.TestCase):

    def test_constructor(self):
        msg = "message"
        b = bytearray(msg, 'utf-8')
        self.assertTrue(type(b is bytearray))
        self.assertEqual(b'message', b)

    def test_fromhex(self):
        hex_str = 'f9cdb9ec44d8d3'
        b = bytearray.fromhex(hex_str)
        self.assertTrue(type(b is bytearray))
        self.assertEqual(b'\xf9\xcd\xb9\xec\x44\xd8\xd3', b)

    def test_to_hex(self):
        b = b'\xf9\xcd\xb9\xec\x44\xd8\xd3'
        hex_str = b.hex()
        self.assertTrue(type(hex_str is str))
        self.assertEqual('f9cdb9ec44d8d3', hex_str)

    def test_list_to_bytearray(self):
        prime_numbers = [2, 3, 5, 7]
        byte_array = bytearray(prime_numbers)
        print(byte_array)

        
if __name__ == '__main__':
    unittest.main()
