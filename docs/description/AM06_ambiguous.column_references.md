# AM06_ambiguous.column_references

Inconsistent column references in ``GROUP BY/ORDER BY`` clauses.

.. note::
   ``ORDER BY`` clauses from ``WINDOW`` clauses are ignored by this rule.

**Anti-pattern**

A mix of implicit and explicit column references are used in a ``GROUP BY``
clause.

.. code-block:: sql
   :force:

    SELECT
        foo,
        bar,
        sum(baz) AS sum_value
    FROM fake_table
    GROUP BY
        foo, 2;

    -- The same also applies to column
    -- references in ORDER BY clauses.

    SELECT
        foo,
        bar
    FROM fake_table
    ORDER BY
        1, bar;

**Best practice**

Reference all ``GROUP BY``/``ORDER BY`` columns either by name or by position.

.. code-block:: sql
   :force:

    -- GROUP BY: Explicit
    SELECT
        foo,
        bar,
        sum(baz) AS sum_value
    FROM fake_table
    GROUP BY
        foo, bar;

    -- ORDER BY: Explicit
    SELECT
        foo,
        bar
    FROM fake_table
    ORDER BY
        foo, bar;

    -- GROUP BY: Implicit
    SELECT
        foo,
        bar,
        sum(baz) AS sum_value
    FROM fake_table
    GROUP BY
        1, 2;

    -- ORDER BY: Implicit
    SELECT
        foo,
        bar
    FROM fake_table
    ORDER BY
        1, 2;
