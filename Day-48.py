3220.Odd_and_even_transactions

SELECT
    transaction_date,
    SUM(CASE WHEN amount % 2 = 1 THEN amount ELSE 0 END) AS odd_sum,
    SUM(CASE WHEN amount % 2 = 0 THEN amount ELSE 0 END) AS even_sum
FROM transactions
GROUP BY transaction_date
ORDER BY transaction_date;

3705.Find_golden_hour_customers
SELECT
    customer_id,
    COUNT(*) AS total_orders,
    ROUND(
        100.0 * SUM(
            CASE
                WHEN HOUR(order_timestamp) BETWEEN 11 AND 13
                  OR HOUR(order_timestamp) BETWEEN 18 AND 20
                THEN 1
                ELSE 0
            END
        ) / COUNT(*),
        0
    ) AS peak_hour_percentage,
    ROUND(AVG(order_rating), 2) AS average_rating
FROM restaurant_orders
GROUP BY customer_id
HAVING COUNT(*) >= 3
   AND SUM(
        CASE
            WHEN HOUR(order_timestamp) BETWEEN 11 AND 13
              OR HOUR(order_timestamp) BETWEEN 18 AND 20
            THEN 1
            ELSE 0
        END
    ) * 100.0 / COUNT(*) >= 60
   AND AVG(order_rating) >= 4.0
   AND COUNT(order_rating) * 100.0 / COUNT(*) >= 50
ORDER BY average_rating DESC, customer_id DESC;