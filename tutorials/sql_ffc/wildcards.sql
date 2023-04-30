--% ends with or starts with 
select * 
from client 
where client_name like '%e';

select * 
from employee
where first_name like 'N%';

-- _ -> a single character 
select * 
from employee
where birth_date like '____-02%';