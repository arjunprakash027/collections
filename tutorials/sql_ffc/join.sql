insert into branch values (4,'buffalo',null,null);

select * from branch;

--find all the branches and its manager name 

select employee.first_name, branch.branch_name
from employee 
inner join branch
on employee.emp_id = branch.mgr_id;

--left join includes all of the rows from left table
select employee.first_name, branch.branch_name
from employee 
left join branch
on employee.emp_id = branch.mgr_id;

--right join includes all of the rows from branch table
select employee.first_name, branch.branch_name
from employee 
right join branch
on employee.emp_id = branch.mgr_id;


select * from branch;

select * from client;

select client.*
from client 
left join branch
on client.branch_id = branch.branch_id;