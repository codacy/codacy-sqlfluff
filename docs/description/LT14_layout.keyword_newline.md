# LT14_layout.keyword_newline

Keyword clauses should follow a standard for being before/after newlines.

**Anti-pattern**

In this example, the keyword are not at the beginning of or alone on the line.

.. code-block:: sql

    SELECT 'a' AS col FROM tab WHERE x = 4 ORDER BY y LIMIT 5

**Best practice**

.. code-block:: sql

    SELECT 'a' AS col
    FROM tab
    WHERE x = 4
    ORDER BY y
    LIMIT 5

.. code-block:: sql

    SELECT 'a' AS col
    FROM
        tab
    WHERE
        x = 4
    ORDER BY
        y
    LIMIT
        5
