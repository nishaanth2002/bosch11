select e1.employee_id,e1.name,e1.salary,e1.department_id
from employees e1
where e1.salary>(
    select avg(e2.salary) from employees e2
    where e2.department_id=e1.department_id
);