# AM07_ambiguous.set_columns

Queries within set query produce different numbers of columns.

**Anti-pattern**

When writing set expressions, all queries must return the same number of columns.

.. code-block:: sql

    WITH cte AS (
        SELECT
            a,
            b
        FROM foo
    )
    SELECT * FROM cte
    UNION
    SELECT
        c,
        d,
        e
     FROM t

**Best practice**

Always specify columns when writing set queries
and ensure that they all seleect same number of columns

.. code-block:: sql

    WITH cte AS (
        SELECT a, b FROM foo
    )
    SELECT
        a,
        b
    FROM cte
    UNION
    SELECT
        c,
        d
    FROM t
