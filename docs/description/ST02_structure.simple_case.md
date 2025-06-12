# ST02_structure.simple_case

Unnecessary ``CASE`` statement.

**Anti-pattern**

``CASE`` statement returns booleans.

.. code-block:: sql
    :force:

    select
        case
            when fab > 0 then true
            else false
        end as is_fab
    from fancy_table

    -- This rule can also simplify CASE statements
    -- that aim to fill NULL values.

    select
        case
            when fab is null then 0
            else fab
        end as fab_clean
    from fancy_table

    -- This also covers where the case statement
    -- replaces NULL values with NULL values.

    select
        case
            when fab is null then null
            else fab
        end as fab_clean
    from fancy_table

**Best practice**

Reduce to ``WHEN`` condition within ``COALESCE`` function.

.. code-block:: sql
    :force:

    select
        coalesce(fab > 0, false) as is_fab
    from fancy_table

    -- To fill NULL values.

    select
        coalesce(fab, 0) as fab_clean
    from fancy_table

    -- NULL filling NULL.

    select fab as fab_clean
    from fancy_table
