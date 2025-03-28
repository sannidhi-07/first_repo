import mysql.connector
from mysql.connector import Error

# Database connection
try:
    db_conn = mysql.connector.connect(
        host="localhost",
        user="your_username",  # Replace with your MySQL username
        password="your_password",  # Replace with your MySQL password
        database="LittleLemonDB"
    )
    cursor = db_conn.cursor()
    print("Connected to Little Lemon database successfully!")
except Error as e:
    print(f"Error: {e}")

# Procedure: GetMaxQuantity
def get_max_quantity():
    cursor.execute("CREATE PROCEDURE GetMaxQuantity() BEGIN SELECT MAX(Quantity) AS MaxQuantity FROM Orders; END;")
    cursor.callproc("GetMaxQuantity")
    for result in cursor.stored_results():
        print("Max Quantity:", result.fetchone()[0])

# Procedure: ManageBooking (Add or check booking)
def manage_booking(customer_id, booking_date, table_number, guests):
    cursor.execute("CREATE PROCEDURE ManageBooking(IN cid INT, IN bdate DATE, IN tnum INT, IN guests INT) "
                   "BEGIN INSERT INTO Bookings (CustomerID, BookingDate, TableNumber, NumberOfGuests) "
                   "VALUES (cid, bdate, tnum, guests); END;")
    cursor.callproc("ManageBooking", (customer_id, booking_date, table_number, guests))
    db_conn.commit()
    print("Booking managed successfully!")

# Procedure: UpdateBooking
def update_booking(booking_id, new_date):
    cursor.execute("CREATE PROCEDURE UpdateBooking(IN bid INT, IN newdate DATE) "
                   "BEGIN UPDATE Bookings SET BookingDate = newdate WHERE BookingID = bid; END;")
    cursor.callproc("UpdateBooking", (booking_id, new_date))
    db_conn.commit()
    print("Booking updated successfully!")

# Procedure: AddBooking
def add_booking(customer_id, booking_date, table_number, guests):
    cursor.execute("CREATE PROCEDURE AddBooking(IN cid INT, IN bdate DATE, IN tnum INT, IN guests INT) "
                   "BEGIN INSERT INTO Bookings (CustomerID, BookingDate, TableNumber, NumberOfGuests) "
                   "VALUES (cid, bdate, tnum, guests); END;")
    cursor.callproc("AddBooking", (customer_id, booking_date, table_number, guests))
    db_conn.commit()
    print("Booking added successfully!")

# Procedure: CancelBooking
def cancel_booking(booking_id):
    cursor.execute("CREATE PROCEDURE CancelBooking(IN bid INT) "
                   "BEGIN DELETE FROM Bookings WHERE BookingID = bid; END;")
    cursor.callproc("CancelBooking", (booking_id,))
    db_conn.commit()
    print("Booking canceled successfully!")

# Test the procedures
get_max_quantity()
manage_booking(1, "2025-03-22", 6, 3)
update_booking(1, "2025-03-23")
add_booking(2, "2025-03-24", 4, 5)
cancel_booking(2)

# Close connection
cursor.close()
db_conn.close()