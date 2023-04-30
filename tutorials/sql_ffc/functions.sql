--total number of emp id in table

select count(emp_id)
from employee;

select count(super_id)
from employee;

select * 
from employee 
where sex = 'F' and birth_date > '2003-01-01';

select count(emp_id)
from employee
where sex = 'F' and birth_date > '2003-01-01';

select avg(salary)
from employee
where sex = 'm';

select sum(salary)
from employee;

select sum(salary)
from employee
where sex = 'f';

select sum(salary)
from employee
where sex = 'm';

--number of males and females in company

select count(sex),sex
from employee
group by sex;

select count(client_name),branch_id
from client
group by branch_id;

-- client id and sum of sales they provide

select client_id, sum(total_sales)
from works_with
group by client_id;

--total sales of each sales man 
select emp_id , sum(total_sales)
from works_with
group by emp_id
order by sum(total_sales) desc;

select *
from employee
join branch;

select employee.first_name,sum(total_sales)
from employee
inner join works_with
on employee.emp_id = works_with.emp_id
group by employee.first_name;

select client.client_name, sum(works_with.total_sales)
from client 
inner join works_with
on works_with.client_id = client.client_id
group by client.client_name;

select employee.first_name,client.client_name,works_with.total_sales
from client 
inner join works_with
on works_with.client_id = client.client_id
inner join employee 
on employee.emp_id = works_with.emp_id;

--max profit branch 

select branch.branch_name , sum(works_with.total_sales)
from branch
inner join employee
on employee.branch_id = branch.branch_id
inner join works_with
on works_with.emp_id = employee.emp_id
group by branch.branch_id;

select * 
from employee
where branch_id = 1;

select * 
from works_with
where emp_id = 106;

