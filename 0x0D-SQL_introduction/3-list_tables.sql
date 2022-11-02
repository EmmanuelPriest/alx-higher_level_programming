-- a script that lists all the tables of a database in your MySQL server
SELECT mysql
FROM information_schema.tables
WHERE table_type='BASE TABLE'
