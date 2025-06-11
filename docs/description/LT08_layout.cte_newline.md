# LT08_layout.cte_newline

Blank line expected but not found after CTE closing bracket.

**Anti-pattern**

There is no blank line after the CTE closing bracket. In queries with many
CTEs, this hinders readability.

.. code-block:: sql

    WITH plop AS (
        SELECT * FROM foo
    )
    SELECT a FROM plop

**Best practice**

Add a blank line.

.. code-block:: sql

    WITH plop AS (
        SELECT * FROM foo
    )

    SELECT a FROM plop
