SELECT category_id,product_name,total_sales FROM (SELECT 
        p.category_id,
        p.product_name,
        SUM(s.sales_amount) AS total_sales,
        RANK() OVER (PARTITION BY p.category_id ORDER BY SUM(s.sales_amount) DESC) AS rnk
    FROM sales s
    JOIN products p ON s.product_id = p.product_id
    GROUP BY p.category_id, p.product_name
) ranked
WHERE rnk = 1;
