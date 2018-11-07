#!/usr/bin/env python3

import unittest
import tempfile

import daughter


class TestDaughter(unittest.TestCase):

    def test_clean_bash_history(self):
        with tempfile.NamedTemporaryFile() as temporary:
            source = ['a', 'b', 'a\t', 'c', 'b ', 'c  ']
            joined_source = '\n'.join(source) + '\n'
            output = ['a', 'b', 'c']
            joined_output = '\n'.join(output) + '\n'
            temporary.write(bytes(joined_source, daughter.ENCODING))
            temporary.flush()
            with open(temporary.name, 'r') as data:
                self.assertEqual(joined_source, data.read())
            daughter.clean_bash_history_of_file(temporary.name)
            with open(temporary.name, 'r') as data:
                self.assertEqual(joined_output, data.read())


if __name__ == '__main__':
    unittest.main()
