-- Total amount spent by each customer, only show customers spending more than $1000, order descending
SELECT c.name, SUM(o.quantity * o.price) AS total_spent
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
GROUP BY c.customer_id
HAVING total_spent > 1000
ORDER BY total_spent DESC;

-- Count orders per customer for orders after Sept 12, 2023
SELECT c.name, COUNT(o.order_id) AS orders_count
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
WHERE o.order_date > '2023-09-12'
GROUP BY c.customer_id
ORDER BY orders_count DESC;

-- List all orders with customer names
SELECT o.order_id, c.name, o.product, o.quantity, o.price, o.order_date
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id
ORDER BY o.order_date;
