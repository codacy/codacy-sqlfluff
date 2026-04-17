# AL10_aliasing.required

Derived tables must have an alias.

A derived table (subquery in a ``FROM`` clause) without an alias will
cause a syntax error in most SQL dialects including MySQL, PostgreSQL,
and T-SQL.

**Anti-pattern**

A subquery in a ``FROM`` clause without an alias.

.. code-block:: sql

    SELECT *
    FROM (
        SELECT 1 AS a
    )

**Best practice**

Add an alias to the derived table.

.. code-block:: sql

    SELECT *
    FROM (
        SELECT 1 AS a
    ) AS derived
