## Function to check if a string is numeric in Postgres

<p><code>
CREATE OR REPLACE FUNCTION isnumeric(text) RETURNS BOOLEAN AS $$ \n
DECLARE X NUMERIC;
BEGIN
  x = $1::NUMERIC;
  RETURN TRUE;
EXCEPTION WHEN others THEN
  RETURN FALSE;
END;
$$
STRICT
LANGUAGE plpgsql IMMUTABLE;
</code></p>

--
