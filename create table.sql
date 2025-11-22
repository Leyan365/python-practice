-- Create customers table
CREATE TABLE customers (
    customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    city TEXT
);

-- Create orders table
CREATE TABLE orders (
    order_id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER,
    product TEXT,
    quantity INTEGER,
    price REAL,
    order_date DATE,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

-- Insert sample data into customers
INSERT INTO customers (name, city) VALUES
('Alice', 'New York'),
('Bob', 'Los Angeles'),
('Charlie', 'Chicago'),
('Diana', 'New York'),
('Eve', 'Los Angeles');

-- Insert sample data into orders
INSERT INTO orders (customer_id, product, quantity, price, order_date) VALUES
(1, 'Laptop', 1, 1200.00, '2023-09-10'),
(1, 'Mouse', 2, 25.00, '2023-09-12'),
(2, 'Monitor', 1, 300.00, '2023-09-11'),
(3, 'Keyboard', 1, 45.00, '2023-09-10'),
(3, 'Mouse', 1, 25.00, '2023-09-15'),
(4, 'Laptop', 2, 1200.00, '2023-09-20'),
(5, 'Desk Chair', 1, 150.00, '2023-09-22');
