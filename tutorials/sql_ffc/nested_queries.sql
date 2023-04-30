--multiple select statements

--name of all the employee who sold over 4k to a single client

select * 
from works_with;

select employee.first_name,works_with.total_sales
from employee
inner join works_with
on employee.emp_id = works_with.emp_id
where works_with.total_sales > 3000;

select employee.first_name, sum(works_with.total_sales)
from employee
inner join works_with
on employee.emp_id = works_with.emp_id
where works_with.total_sales > 3000
group by employee.first_name
limit 2ff;


--nested

select works_with.emp_id
from works_with
where works_with.total_sales > 3000;

select employee.first_name
from employee
where employee.emp_id in (
    select works_with.emp_id
    from works_with
    where works_with.total_sales > 3000
);

--find all client handles by brnach that arjun manages 

select client.client_name,branch.branch_name
from client
inner join branch 
on client.branch_id = branch.branch_id
inner join employee
on employee.emp_id = branch.mgr_id 
where employee.first_name = 'arjun';


select client.client_name, branch.branch_name 
from client 
inner join branch
on client.branch_id = branch.branch_id
where client.branch_id in (
    select branch.branch_id
    from branch
    where branch.mgr_id = 100
);