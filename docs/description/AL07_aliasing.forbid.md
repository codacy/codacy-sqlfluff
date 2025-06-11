# AL07_aliasing.forbid

Avoid table aliases in from clauses and join conditions.

.. note::
   This rule was taken from the `dbt Style Guide
   <https://github.com/dbt-labs/corp/blob/main/dbt_style_guide.md>`_
   which notes that:

    Avoid table aliases in join conditions (especially initialisms) - it's
    harder to understand what the table called "c" is compared to "customers".

   This rule is controversial and for many larger databases avoiding alias is
   neither realistic nor desirable. In particular for BigQuery due to the
   complexity of backtick requirements and determining whether a name refers
   to a project or dataset so automated fixes can potentially break working
   SQL code. For most users :sqlfluff:ref:`AL06` is likely a more appropriate
   linting rule to drive a sensible behaviour around aliasing.

   The stricter treatment of aliases in this rule may be useful for more
   focused projects, or temporarily as a refactoring tool because the
   :code:`fix` routine of the rule can remove aliases.

   This rule is disabled by default for all dialects it can be enabled with
   the ``force_enable = True`` flag.

**Anti-pattern**

In this example, alias ``o`` is used for the orders table, and ``c`` is used for
``customers`` table.

.. code-block:: sql

    SELECT
        COUNT(o.customer_id) as order_amount,
        c.name
    FROM orders as o
    JOIN customers as c on o.id = c.user_id


**Best practice**

Avoid aliases.

.. code-block:: sql

    SELECT
        COUNT(orders.customer_id) as order_amount,
        customers.name
    FROM orders
    JOIN customers on orders.id = customers.user_id

    -- Self-join will not raise issue

    SELECT
        table1.a,
        table_alias.b,
    FROM
        table1
        LEFT JOIN table1 AS table_alias ON
            table1.foreign_key = table_alias.foreign_key
