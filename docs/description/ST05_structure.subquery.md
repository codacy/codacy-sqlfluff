# ST05_structure.subquery

Join/From clauses should not contain subqueries. Use CTEs instead.

By default this rule is configured to allow subqueries within ``FROM``
clauses but not within ``JOIN`` clauses. If you prefer a stricter lint
then this is configurable.

.. note::
   Some dialects don't allow CTEs, and for those dialects
   this rule makes no sense and should be disabled.

**Anti-pattern**

.. code-block:: sql

    select
        a.x, a.y, b.z
    from a
    join (
        select x, z from b
    ) using(x)


**Best practice**

.. code-block:: sql

    with c as (
        select x, z from b
    )
    select
        a.x, a.y, c.z
    from a
    join c using(x)
