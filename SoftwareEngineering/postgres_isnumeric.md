## Function to check if a string is numeric in Postgres

```
CREATE OR REPLACE FUNCTION isnumeric(text) RETURNS BOOLEAN AS $$
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
```

--
