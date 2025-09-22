SELECT region, customer_id, order_count
FROM (
    SELECT region, customer_id, COUNT(*) AS order_count,
           RANK() OVER (PARTITION BY region ORDER BY COUNT(*) DESC) AS rnk
    FROM orders
    GROUP BY region, customer_id
) ranked
WHERE rnk = 1;
