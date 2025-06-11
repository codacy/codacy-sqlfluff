# CV12_convention.join_condition

Use `JOIN ... ON ...` instead of `WHERE ...` for join conditions.

**Anti-pattern**

Using WHERE clause for join conditions.

.. code-block:: sql

    SELECT
        foo.a
        , bar.b
    FROM foo
    JOIN bar
    WHERE foo.x = bar.y;

**Best practice**

Use JOIN ON clause for join condition.

.. code-block:: sql

    SELECT
        foo.a
        , bar.b
    FROM foo
    JOIN bar
    ON foo.x = bar.y;
