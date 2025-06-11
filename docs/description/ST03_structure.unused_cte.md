# ST03_structure.unused_cte

Query defines a CTE (common-table expression) but does not use it.

**Anti-pattern**

Defining a CTE that is not used by the query is harmless, but it means
the code is unnecessary and could be removed.

.. code-block:: sql

    WITH cte1 AS (
      SELECT a
      FROM t
    ),
    cte2 AS (
      SELECT b
      FROM u
    )

    SELECT *
    FROM cte1

**Best practice**

Remove unused CTEs.

.. code-block:: sql

    WITH cte1 AS (
      SELECT a
      FROM t
    )

    SELECT *
    FROM cte1
