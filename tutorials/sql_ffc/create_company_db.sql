create table employee(
    emp_id int primary key,
    first_name varchar(30),
    last_name varchar(30),
    birth_date date,
    sex varchar(1),
    salary int,
    super_id int,
    branch_id int
);
drop table employee;

create table branch(
    branch_id int primary key,
    branch_name varchar(40),
    mgr_id int,
    mgr_start_date date,
    foreign key(mgr_id) references employee(emp_id) on delete set null
);
drop table branch;

alter table employee
add foreign key(branch_id)
references branch(branch_id)
on delete set null;

alter table employee
add foreign key(super_id)
references employee(emp_id)
on delete set null;

create table client(
    client_id int primary key,
    client_name varchar(30),
    branch_id int,
    foreign key(branch_id) references branch(branch_id) on delete set null
);
drop table client;

create table works_with(
    emp_id int,
    client_id int,
    total_sales int,
    primary key(emp_id,client_id),
    foreign key(emp_id) references employee(emp_id) on delete cascade,
    foreign key(client_id) references client(client_id) on delete cascade
); 

create table branch_supplier(
    branch_id int,
    supplier_name varchar(40),
    supply_type varchar(40),
    primary key(branch_id,supplier_name),
    foreign key(branch_id) references branch(branch_id) on delete cascade
);

--insert datas

insert into employee values(100,'Arjun','Rao','2002-02-01','M',250000,NULL,NULL);
insert into branch values(1,'software',100,'2022-02-01');
update employee
set branch_id = 1
where emp_id = 100;

insert into employee values(101,'raju','Rao','2002-02-01','M',250000,100,1);


insert into employee values(103,'Naveen','Kumar','2003-04-29','F',4566,NULL,NULL);
insert into branch values(2,'management',103,'2022-02-01');
update employee
set branch_id = 2
where emp_id = 103;

insert into employee values(104,'Naresh','Kumar','2001-03-04','M',5000,NULL,NULL);
insert into branch values(3,'cloud',104,'2022-02-03');
update employee
set branch_id = 3
where emp_id = 104;

update employee
set super_id = 100
where emp_id = 103 or emp_id = 104;

insert into employee values(105,'mamu','Rao','2002-02-01','F',25000,103,1);
insert into employee values(106,'somu','Rao','2002-02-01','M',25000,103,1);
insert into employee values(107,'pamu','Rao','2002-02-01','F',25000,104,2);
insert into employee values(108,'jomu','Rao','2002-02-01','M',50000,104,2);
insert into employee values(109,'gomu','Rao','2002-02-01','F',20000,100,3);
insert into employee values(110,'domu','Rao','2002-02-01','F',25000,103,3);
insert into employee values(111,'lamu','Rao','2002-02-01','M',25000,103,3);

select * from employee;

--branch supplier

insert into branch_supplier values(1,'Github','CICD');
insert into branch_supplier values(1,'docker','development');
insert into branch_supplier values(1,'python','development');
insert into branch_supplier values(2,'JIRA','agile process');
insert into branch_supplier values(2,'trello','kanban');
insert into branch_supplier values(2,'zoho','collabration');
insert into branch_supplier values(3,'GCP','Infrastructure');
insert into branch_supplier values(3,'Azure','clusters');
insert into branch_supplier values(3,'AWS','scaling');

select * from branch_supplier;

--client table

insert into client values(401,'TCS',1);
insert into client values(402,'Accenture',1);
insert into client values(403,'google',2);
insert into client values(404,'amazon',2);
insert into client values(405,'goldman shacs',3);

select * from client;

--works with table
insert into works_with values(105,401,3000);
insert into works_with values(105,402,300);
insert into works_with values(106,402,1000);
insert into works_with values(108,402,4000);
insert into works_with values(110,404,334500);
insert into works_with values(111,403,3003);
insert into works_with values(111,405,3002);
insert into works_with values(103,405,30011);
insert into works_with values(104,403,300045);
insert into works_with values(107,401,3004);

select * from works_with;