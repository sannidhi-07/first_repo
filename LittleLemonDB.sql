-- Create the Little Lemon database
CREATE DATABASE LittleLemonDB;
USE LittleLemonDB;

-- Customers table
CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY AUTO_INCREMENT,
    FullName VARCHAR(100) NOT NULL,
    ContactNumber VARCHAR(15),
    Email VARCHAR(100)
);

-- Bookings table
CREATE TABLE Bookings (
    BookingID INT PRIMARY KEY AUTO_INCREMENT,
    CustomerID INT,
    BookingDate DATE NOT NULL,
    TableNumber INT NOT NULL,
    NumberOfGuests INT NOT NULL,
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID)
);

-- Orders table (for GetMaxQuantity procedure)
CREATE TABLE Orders (
    OrderID INT PRIMARY KEY AUTO_INCREMENT,
    BookingID INT,
    Quantity INT NOT NULL,
    TotalCost DECIMAL(10, 2),
    FOREIGN KEY (BookingID) REFERENCES Bookings(BookingID)
);

-- Insert sample data
INSERT INTO Customers (FullName, ContactNumber, Email) VALUES
('John Doe', '123-456-7890', 'john.doe@example.com'),
('Jane Smith', '098-765-4321', 'jane.smith@example.com');

INSERT INTO Bookings (CustomerID, BookingDate, TableNumber, NumberOfGuests) VALUES
(1, '2025-03-20', 5, 4),
(2, '2025-03-21', 3, 2);

INSERT INTO Orders (BookingID, Quantity, TotalCost) VALUES
(1, 10, 50.00),
(2, 5, 25.00);