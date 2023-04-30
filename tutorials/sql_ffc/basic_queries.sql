select * from branch;

--find all employees

select * 
from employee;

select *
from client;

select * 
from employee
order by salary desc;

select *
from employee
order by sex,first_name,last_name; --this query orders by female first, then inside that orders by name.

--only first 5 employee is returned
select * 
from employee
order by salary desc 
limit 4;

--converts first_name to forename and last_name to surname 
select first_name as forename , last_name as surname
from employee;

--figure out all different genders
select distinct sex 
from employee;

select distinct supplier_name
from branch_supplier;

select distinct branch_name
from branch;


