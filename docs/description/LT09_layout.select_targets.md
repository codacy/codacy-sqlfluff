# LT09_layout.select_targets

Select targets should be on a new line unless there is only one select target.

.. note::
   By default, a wildcard (e.g. ``SELECT *``) is considered a single select target.
   If you want it to be treated as multiple select targets, configure
   ``wildcard_policy = multiple``.

**Anti-pattern**

Multiple select targets on the same line.

.. code-block:: sql

    select a, b
    from foo;

    -- Single select target on its own line.

    SELECT
        a
    FROM foo;


**Best practice**

Multiple select targets each on their own line.

.. code-block:: sql

    select
        a,
        b
    from foo;

    -- Single select target on the same line as the ``SELECT``
    -- keyword.

    SELECT a
    FROM foo;

    -- When select targets span multiple lines, however they
    -- can still be on a new line.

    SELECT
        SUM(
            1 + SUM(
                2 + 3
            )
        ) AS col
    FROM test_table;
