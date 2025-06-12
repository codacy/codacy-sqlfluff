# AM04_ambiguous.column_count

Query produces an unknown number of result columns.

**Anti-pattern**

Querying all columns using ``*`` produces a query result where the number
or ordering of columns changes if the upstream table's schema changes.
This should generally be avoided because it can cause slow performance,
cause important schema changes to go undetected, or break production code.
For example:

* If a query does ``SELECT t.*`` and is expected to return columns ``a``, ``b``,
  and ``c``, the actual columns returned will be wrong/different if columns
  are added to or deleted from the input table.
* ``UNION`` and ``DIFFERENCE`` clauses require the inputs have the same number
  of columns (and compatible types).
* ``JOIN`` queries may break due to new column name conflicts, e.g. the
  query references a column ``c`` which initially existed in only one input
  table but a column of the same name is added to another table.
* ``CREATE TABLE (<<column schema>>) AS SELECT *``


.. code-block:: sql

    WITH cte AS (
        SELECT * FROM foo
    )

    SELECT * FROM cte
    UNION
    SELECT a, b FROM t

**Best practice**

Somewhere along the "path" to the source data, specify columns explicitly.

.. code-block:: sql

    WITH cte AS (
        SELECT * FROM foo
    )

    SELECT a, b FROM cte
    UNION
    SELECT a, b FROM t
