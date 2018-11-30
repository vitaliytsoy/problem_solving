-- Schema:
-- Create table If Not Exists Person (Id int, Email varchar(255))
-- Truncate table Person
-- insert into Person (Id, Email) values ('1', 'a@b.com')
-- insert into Person (Id, Email) values ('2', 'c@d.com')
-- insert into Person (Id, Email) values ('3', 'a@b.com')

-- Description:
-- Write a SQL query to find all duplicate emails in a table named Person.


Select Email
From person 
Group by Email
Having count(Email)>1
