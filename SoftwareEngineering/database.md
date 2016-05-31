## All the database related TILs go here

Import tab delimited data from files in postgres:
```
copy foo from '/tmp/foo.txt' with (format csv, delimiter E'\t')
```
--

### Postgres - delete duplicates by id

```
DELETE FROM tablename
WHERE id IN (SELECT id
              FROM (SELECT id,
                             ROW_NUMBER() OVER (partition BY column1, column2, column3 ORDER BY id) AS rnum
                     FROM tablename) t
              WHERE t.rnum > 1);
```

--
