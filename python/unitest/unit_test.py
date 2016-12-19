#unit test

import unittest
from mydict_test import mydict

class TestMydict(unittest.TestCase):

    def setUp(self):
        print('set up ...')

    def tearDown(self):
        print('tear down ...')

    def test_init(self):
        d = mydict(a = 1, b = 'test')
        self.assertEqual(d.a, 1)
        self.assertEqual(d.b, 'test')
        self.assertTrue(isinstance(d, dict))

    def test_key(self):
        d = mydict()
        d['key'] = 'value'
        self.assertEqual(d.key, 'value')

    def test_attr(self):
        d = mydict()
        d.key = 'value'
        self.assertTrue('key' in d)
        self.assertEqual(d['key'], 'value')

    def test_keyerror(self):
        d = mydict()
        with self.assertRaises(KeyError):
            value = d['empty']

    def test_attrerror(self):
        d = mydict()
        with self.assertRaises(AttributeError):
            value = d.empty



    


if __name__ == '__main__':
    unittest.main()