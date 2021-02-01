# Tests for SeatTheater by Nathan Taylor
# Last updated 2/1/2021

import unittest
from SeatTheater import SeatTheater, ExcessRowError

class TestSeatTheater(unittest.TestCase):
    """
    Tests for the SeatTheater class.
    """

    def setUp(self):
        "Example test file"

        self.test_file = "test_reservations.txt"
        self.theater = SeatTheater(self.test_file)
        self.bad_test_file = "bad_reservations.txt"

    def test_init(self):
        """
        Test initialization of the SeatTheater class.
        """

        # check row and column lists are ok
        self.assertEqual(self.theater._row_list, ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'])
        self.assertEqual(self.theater._col_list, ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', \
            '11', '12', '13', '14', '15', '16', '17', '18', '19', '20'])

        # test too many rows 
        with self.assertRaises(ExcessRowError):
            x = SeatTheater(self.test_file, rows=27)

        # test file parsing errors
        x = SeatTheater("not a file")
        self.assertEqual(x._reservations, [])

        x = SeatTheater(self.bad_test_file)
        self.assertEqual(x._reservations, [])

        # check that reservation list is ok
        self.assertEqual(self.theater._reservations, [("R001", 2), ("R002", 4)])


unittest.main()