# AL04_aliasing.unique.table

Table aliases should be unique within each clause.

Reusing table aliases is very likely a coding error.

**Anti-pattern**

In this example, the alias ``t`` is reused for two different tables:

.. code-block:: sql

    SELECT
        t.a,
        t.b
    FROM foo AS t, bar AS t

    -- This can also happen when using schemas where the
    -- implicit alias is the table name:

    SELECT
        a,
        b
    FROM
        2020.foo,
        2021.foo

**Best practice**

Make all tables have a unique alias.

.. code-block:: sql

    SELECT
        f.a,
        b.b
    FROM foo AS f, bar AS b

    -- Also use explicit aliases when referencing two tables
    -- with the same name from two different schemas.

    SELECT
        f1.a,
        f2.b
    FROM
        2020.foo AS f1,
        2021.foo AS f2
