port unittest

ass StringTestCase(unittest.TestCase):

    def test_string_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')
        self.assertTrue('bar'.upper()=='BAR')
        with self.assertRaises(TypeError):
            s = 12
            s.upper()

    def test_string_length(self):
        self.assertEqual(len('Portland'), 8)
        self.assertTrue(len('Willamette')>7)


    __name__ == '__main__':
    unittest.main()
