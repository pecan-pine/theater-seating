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

    def __init__(self, reservation_file, rows=10, cols=20, initial_row=4, row_buffer=1, col_buffer=3):
        """
        Initialize a SeatTheater object with a given reservation_file,
        number of rows (default 10), number of columns (default 20),
        initial row for customers to be placed in (default 4),
        row buffer (default 1), and column buffer (default 3).
        """

        self._row_list = self.make_row_list(rows)
        self._col_list = self.make_column_list(cols)

        self._row_buffer = row_buffer
        self._col_buffer = col_buffer

        self._reservations = self.make_reservation_list(reservation_file)


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

        return [str(col + 1) for col in range(cols)]

    def make_reservation_list(self, reservation_file):
        """
        Returns a list of tuples (reservation_name, number_of_guests)
        of reservations parsed from the reservation_file. Assumes the 
        reservation_file has the form "R123 8", where R123 is the reservation 
        name and 8 is the number of guests.
        """

        reservations = []

        try:
            with open(reservation_file, 'r') as reservation_data:
                for reservation_datum in reservation_data:
                    reservation_name, text_number = reservation_datum.split()
                    reservation_number = int(text_number)
                    reservations.append((reservation_name, reservation_number))
        except FileNotFoundError:
            if __name__ == "__main__":
                print("We could not find your reservation file.")
            return []
        except ValueError:
            if __name__ == "__main__":
                print("We could not parse part of your reservation file. Is it in the correct format?")
            return []
        except:
            if __name__ == "__main__":
                print("Something went wrong. Please try again.")
            return []

        return reservations
    
    def guest_placement(self):
        """
        Returns an ordered list of placements for guests.
        """

        return [("R001", ["I1", "I2"]), ("R002", ["F16", "F17"])]

    def seat_theater(self, output_file="seating_placement.txt"):
        """
        Writes an output file of the theater seating placements.
        """

        with open(output_file, 'w') as output:
            for guest_data in self.guest_placement():
                guest, seats = guest_data
                seats = ", ".join(seats)
                output.write(guest + " " + seats + "\n")



if __name__ == "__main__":
    st = SeatTheater("reservations.txt")

    print(st._reservations)

    print(st._row_list)
    print(st._col_list)
    st.seat_theater()
