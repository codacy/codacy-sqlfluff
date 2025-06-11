# AL06_aliasing.length

Enforce table alias lengths in from clauses and join conditions.

**Anti-pattern**

In this example, alias ``o`` is used for the orders table.

.. code-block:: sql

    SELECT
        SUM(o.amount) as order_amount,
    FROM orders as o


**Best practice**

Avoid aliases. Avoid short aliases when aliases are necessary.

See also: :sqlfluff:ref:`AL07`.

.. code-block:: sql

    SELECT
        SUM(orders.amount) as order_amount,
    FROM orders

    SELECT
        replacement_orders.amount,
        previous_orders.amount
    FROM
        orders AS replacement_orders
    JOIN
        orders AS previous_orders
        ON replacement_orders.id = previous_orders.replacement_id
