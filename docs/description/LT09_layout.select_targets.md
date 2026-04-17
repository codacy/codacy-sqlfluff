# LT09_layout.select_targets

Select targets should be on a new line unless there is only one select target.

.. note::
   By default, a wildcard (e.g. ``SELECT *``) is considered a single select target.
   If you want it to be treated as multiple select targets, configure
   ``wildcard_policy = multiple``.

.. note::
   By default (``single_target_policy = same_line``), a single select target
   is allowed to remain on the same line as the ``SELECT`` keyword (e.g.
   ``SELECT a FROM foo``). If you want *all* select targets, including single
   ones, to be placed on a new line set ``single_target_policy = new_line``.
   This gives consistent formatting regardless of the number of select targets.

**Anti-pattern**

Multiple select targets on the same line.

.. code-block:: sql

    select a, b
    from foo;

    -- Single select target on its own line
    -- (with default ``single_target_policy = same_line``).

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
    -- keyword (with default ``single_target_policy = same_line``).

    SELECT a
    FROM foo;

    -- With ``single_target_policy = new_line``, single select
    -- targets must also be on a new line for consistency.

    SELECT
        a
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
