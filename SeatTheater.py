# A theater-seating program by Nathan Taylor
# Last updated 2/1/2021

class ExcessRowError(Exception):
    """
    An exception raised when there are too many rows (more than 26). 
    """
    pass

class SeatTheater:
    """
    A class to determine an optimal seating arrangement in a theater. 
    """

    def make_row_list(self, rows):
        """
        Convert the number of rows to a list of letters. 
        Raises an ExcessRowError if there are more than 26 rows. 
        """

        if rows > 26:
            raise ExcessRowError

        row_list = []

        for row in range(rows):
            row_list.append(chr(ord('A') + row))

        return row_list

    def make_column_list(self, cols):
        """
        Convert the number of columns to a list of numbers.
        """

        return [col + 1 for col in range(cols)]

    def __init__(self, reservation_file, rows=10, cols=20, row_buffer=1, col_buffer=3):
        """
        Initialize a SeatTheater object with a given reservation_file,
        number of rows (default 10), number of columns (default 20),
        row buffer (default 1), and column buffer (default 3).
        """

        try:
            self._row_list = self.make_row_list(rows)
            self._col_list = self.make_column_list(cols)
        except:
            print("We could not parse your theater row/column data. Did you provide more than 26 rows?")
            return

        self._reservation_file = reservation_file
        self._row_buffer = row_buffer
        self._col_buffer = col_buffer


if __name__ == "__main__":
    st = SeatTheater("hello")

    print(st._row_list)
    print(st._col_list)
