# AL08_aliasing.unique.column

Column aliases should be unique within each clause.

Reusing column aliases is very likely a coding error. Note that while
in many dialects, quoting an identifier makes it case-sensitive
this rule always compares in a case-insensitive way. This is because
columns with the same name, but different case, are still confusing
and potentially ambiguous to other readers.

In situations where it is *necessary* to have columns with the same
name (whether they differ in case or not) we recommend disabling this
rule for either just the line, or the whole file.

**Anti-pattern**

In this example, the alias ``foo`` is reused for two different columns:

.. code-block:: sql

    SELECT
        a as foo,
        b as foo
    FROM tbl;

    -- This can also happen when referencing the same column
    -- column twice, or aliasing an expression to the same
    -- name as a column:

    SELECT
        foo,
        foo,
        a as foo
    FROM tbl;

**Best practice**

Make all columns have a unique alias.

.. code-block:: sql

    SELECT
        a as foo,
        b as bar
    FROM tbl;

    -- Avoid also using the same column twice unless aliased:

    SELECT
        foo as foo1,
        foo as foo2,
        a as foo3
    FROM tbl;
