import unittest

class EncodeDecode(unittest.TestCase):

    def test_encode(self):
        msg = 'message'
        b = msg.encode('utf-8')
        self.assertTrue(type(msg is str))
        self.assertTrue(type(b is bytes))

    def test_decode(self):
        b = bytes.fromhex('6d657373616765')
        s = b.decode('utf-8')
        self.assertTrue(type(b is bytes))
        self.assertTrue(type(s is str))
        self.assertEqual('message', s)


if __name__ == '__main__':
    unittest.main()
