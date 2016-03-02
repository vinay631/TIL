## All the database related TILs go here

Import tab delimited data from files in postgres:

copy foo from '/tmp/foo.txt' with (format csv, delimiter E'\t')

--
