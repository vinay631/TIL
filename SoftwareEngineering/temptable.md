## Temporary table in Postgres

Temporary tables are automatically dropped at the end of a session or the current transaction. Vacuum and analyze operations are not performed automatically on temporary table. So for complex queries using temporary tables, it is good to run ANALYZE on temp tables after they are created.

<p><code>
CREATE TEMP TABLE FOO ...
</code></p>

--
