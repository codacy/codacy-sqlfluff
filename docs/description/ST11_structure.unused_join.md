# ST11_structure.unused_join

Joined table not referenced in query.

This rule will check if there are any tables that are referenced in the
``FROM`` or ``JOIN`` clause of a ``SELECT`` statement, but where no
columns from that table are referenced in the any of the other clauses.
Because some types of join are often used as filters, or to otherwise
control granularity without being referenced (e.g. ``INNER`` and ``CROSS``),
this rule only applies to explicit ``OUTER`` joins (i.e. ``LEFT``, ``RIGHT``
and ``FULL`` joins).

This rule relies on all of the column references in the ``SELECT``
statement being qualified with at least the table name, and so is
designed to work alongside :sqlfluff:ref:`references.qualification`
(:sqlfluff:ref:`RF02`). This is because without the knowledge of what
columns exist in each upstream table, the rule is unable to resolve
which table an unqualified column reference is pulled from.

This rule does not propose a fix, because it assumes that it an unused
table is a mistake, but doesn't know whether the mistake was the join,
or the mistake was not using it.

**Anti-pattern**

In this example, the table ``bar`` is included in the ``JOIN`` clause
but not columns from it are referenced in

.. code-block:: sql

    SELECT
        foo.a,
        foo.b
    FROM foo
    LEFT JOIN bar ON foo.a = bar.a

**Best practice**

Remove the join, or use the table.

.. code-block:: sql

    SELECT foo.a, vee.b
    FROM foo;

    SELECT
        foo.a,
        foo.b,
        bar.c
    FROM foo
    LEFT JOIN bar ON foo.a = bar.a

In the (*very rare*) situations that it is logically necessary to include
a table in a join clause, but not otherwise refer to it (likely for
granularity reasons, or as a stepping stone to another table), we recommend
ignoring this rule for that specific line by using ``-- noqa: ST11`` at
the end of the line.

.. note:

   To avoid sticky situations with casing and quoting in different dialects
   this rule uses case-insensitive comparison. That means if you have two
   tables with the same name, but different cases (and you're really sure
   that's a good idea!), then this rule may not detect if one of them is
   unused.
