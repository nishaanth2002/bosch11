select p.product_id,p.product_name
from products p
where p.product_id not in (
    select distinct product_id from orders
);