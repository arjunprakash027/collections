select first_name 
from employee;

select branch_name 
from branch;

--combine both into same query

select first_name as company_details
from employee
union
select branch_name 
from branch;

select sum(salary)
from employee
union 
select sum(total_sales)
from works_with;

