# AM09_ambiguous.order_by_limit

Use of LIMIT and OFFSET without ORDER BY may lead to non-deterministic results.

When using ``LIMIT`` or ``OFFSET``, it's generally recommended to include
an ``ORDER BY`` clause to ensure deterministic results.

**Anti-pattern**

The following query has LIMIT and OFFSET without ORDER BY, which may return
different results in successive executions.

.. code-block:: sql

    SELECT *
    FROM foo
    LIMIT 10 OFFSET 5;

**Best practice**

Include an ``ORDER BY`` clause:

.. code-block:: sql

    SELECT *
    FROM foo
    ORDER BY id
    LIMIT 10 OFFSET 5;
