# RF07_references.window_alias

Do not reference a column alias inside its own ``OVER`` clause.

Window functions are evaluated before the ``SELECT`` list aliases are
applied, so an unqualified reference in a ``PARTITION BY`` or ``ORDER BY``
which happens to match an alias does not resolve to that alias. When more
than one table is in scope it silently resolves to a real column on one of
them instead, changing the result without any error.

.. note::
   This rule is disabled by default. Enable it with the
   ``force_enable = True`` flag.

**Anti-pattern**

``id`` is an alias for ``t1.col1``, but inside the window it resolves to
``t2.id`` from the joined table.

.. code-block:: sql

    SELECT
        t1.col1 AS id,
        ROW_NUMBER() OVER (PARTITION BY id ORDER BY t1.ts) AS rn
    FROM t1
    LEFT JOIN t2 ON t1.col1 = t2.id

**Best practice**

Qualify the reference with its table so the intended column is used.

.. code-block:: sql

    SELECT
        t1.col1 AS id,
        ROW_NUMBER() OVER (PARTITION BY t1.col1 ORDER BY t1.ts) AS rn
    FROM t1
    LEFT JOIN t2 ON t1.col1 = t2.id
