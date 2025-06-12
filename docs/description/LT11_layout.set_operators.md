# LT11_layout.set_operators

Set operators should be surrounded by newlines.

**Anti-pattern**

In this example, `UNION ALL` is not on a line itself.

.. code-block:: sql

    SELECT 'a' AS col UNION ALL
    SELECT 'b' AS col

**Best practice**

.. code-block:: sql

    SELECT 'a' AS col
    UNION ALL
    SELECT 'b' AS col
