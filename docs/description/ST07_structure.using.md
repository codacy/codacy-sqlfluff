# ST07_structure.using

Prefer specifying join keys instead of using ``USING``.

.. note::
   This rule was originally taken from the `dbt Style Guide
   <https://github.com/dbt-labs/corp/blob/ main/dbt_style_guide.md>`_
   which notes that:

    Certain warehouses have inconsistencies in ``USING``
    results (specifically Snowflake).

   In fact `dbt removed it from their style guide in February 2022
   <https://github.com/dbt-labs/corp/pull/58>`_. However, some like the
   rule, so for now we will keep it in SQLFluff, but encourage those that
   do not find value in the rule, to turn it off.

.. note::

   This rule is disabled for ClickHouse as it supports ``USING`` without
   brackets which this rule does not support.

**Anti-pattern**

.. code-block:: sql

    SELECT
        table_a.field_1,
        table_b.field_2
    FROM
        table_a
    INNER JOIN table_b USING (id)

**Best practice**

Specify the keys directly

.. code-block:: sql

    SELECT
        table_a.field_1,
        table_b.field_2
    FROM
        table_a
    INNER JOIN table_b
        ON table_a.id = table_b.id
