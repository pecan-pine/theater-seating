# Tests for SeatTheater by Nathan Taylor
# Last updated 2/1/2021

import unittest
from SeatTheater import SeatTheater

class TestSeatTheater(unittest.TestCase):
    """
    Tests for the SeatTheater class.
    """

    def test_init(self):
        """
        Test initialization of the SeatTheater class.
        """

        x = SeatTheater("testing")
        self.assertEqual(x._row_list, ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'])
        self.assertEqual(x._col_list, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])

unittest.main()