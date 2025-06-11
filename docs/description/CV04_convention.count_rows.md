# CV04_convention.count_rows

Use consistent syntax to express "count number of rows".

Note:
    If both ``prefer_count_1`` and ``prefer_count_0`` are set to true
    then ``prefer_count_1`` has precedence.

``COUNT(*)``, ``COUNT(1)``, and even ``COUNT(0)`` are equivalent syntaxes
in many SQL engines due to optimizers interpreting these instructions as
"count number of rows in result".

The ANSI-92_ spec mentions the ``COUNT(*)`` syntax specifically as
having a special meaning:

    If COUNT(*) is specified, then
    the result is the cardinality of T.

So by default, `SQLFluff` enforces the consistent use of ``COUNT(*)``.

If the SQL engine you work with, or your team, prefers ``COUNT(1)`` or
``COUNT(0)`` over ``COUNT(*)``, you can configure this rule to consistently
enforce your preference.

.. _ANSI-92: http://msdn.microsoft.com/en-us/library/ms175997.aspx

**Anti-pattern**

.. code-block:: sql

    select
        count(1)
    from table_a

**Best practice**

Use ``count(*)`` unless specified otherwise by config ``prefer_count_1``,
or ``prefer_count_0`` as preferred.

.. code-block:: sql

    select
        count(*)
    from table_a
