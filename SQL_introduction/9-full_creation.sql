-- Write a script that creates a table second_table in the database hbtn_0c_0 in your MySQL server and add multiples rows.
CREATE TABLE IF NOT EXISTS second_table (
    id int,
    name varchar(256),
    score int
);