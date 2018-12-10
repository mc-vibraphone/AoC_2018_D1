import unittest
import json

from freq_calc import FreqCalc

import logging
logging.basicConfig(level=logging.DEBUG)
LOG = logging.getLogger()


class FreqCalcTest(unittest.TestCase):
    def test_results(self):
        with open('./d1_small.json', 'rt') as _file:
            test_data = json.load(_file)
        for t in test_data:
            tested = FreqCalc(t['input'].split())
            LOG.info('Testing %s :: it should be [%s]', t['input'], t['output'])

            self.assertEqual(tested.final_freq, t['output'])


if __name__ == '__main__':
    print('Let\'s go!')
    unittest.main()

