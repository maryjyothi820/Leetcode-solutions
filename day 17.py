183.customers who never order
SELECT name AS Customers
FROM Customers
WHERE id NOT IN (
    SELECT customerId FROM Orders
);
182.duplicate eamils
SELECT email AS Email
FROM Person
GROUP BY email
HAVING COUNT(email) > 1;