# LT15_layout.newlines

Too many consecutive blank lines.

**Anti-pattern**

In this example, the maximum number of empty lines inside a statement is set to 0.

.. code-block:: sql

    SELECT 'a' AS col
    FROM tab


    WHERE x = 4
    ORDER BY y


    LIMIT 5
    ;

**Best practice**

.. code-block:: sql

    SELECT 'a' AS col
    FROM tab
    WHERE x = 4
    ORDER BY y
    LIMIT 5
    ;
