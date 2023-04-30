--createing a table to record logs
create table trigger_test(
    message varchar(100)
);

select *
FROM trigger_test;

delimiter $$
create
     trigger my_trigger before insert
     on employee
     for each row 
     begin 
        insert into trigger_test values('new employee added');
     end $$
delimiter ;

--using ifelse

delimiter $$

create
    trigger new_trigger before insert
    on employee
    for each row 
    begin
        if NEW.sex = 'M' then
        insert into trigger_test values ('added a male employee');
        elseif NEW.sex = 'F' then
        insert into trigger_test values ('added a female employee');
        else
        insert into trigger_test values ('added a trans');
        end if;
    end $$

delimiter ;

alter table trigger_test
add name varchar(20);

describe trigger_test;


