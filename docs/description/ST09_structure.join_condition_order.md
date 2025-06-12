# ST09_structure.join_condition_order

Joins should list the table referenced earlier/later first.

This rule will break conditions from join clauses down into subconditions
using the "and" and "or" binary operators.

Subconditions that are made up of a qualified column reference,
a comparison operator and another qualified column reference
are then evaluated to check whether they list the table that was referenced
earlier - or later, depending on the ``preferred_first_table_in_join_clause``
configuration.

Subconditions that do not follow that pattern are ignored by this rule.

.. note::
   Joins in ``WHERE`` clauses are currently not supported by this rule.

**Anti-pattern**

In this example, the tables that were referenced later are listed first
and the ``preferred_first_table_in_join_clause`` configuration
is set to ``earlier``.

.. code-block:: sql

    select
        foo.a,
        foo.b,
        bar.c
    from foo
    left join bar
        -- This subcondition does not list
        -- the table referenced earlier first:
        on bar.a = foo.a
        -- Neither does this subcondition:
        and bar.b = foo.b

**Best practice**

List the tables that were referenced earlier first.

.. code-block:: sql

    select
        foo.a,
        foo.b,
        bar.c
    from foo
    left join bar
        on foo.a = bar.a
        and foo.b = bar.b
