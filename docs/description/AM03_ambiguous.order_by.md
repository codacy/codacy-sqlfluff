# AM03_ambiguous.order_by

Ambiguous ordering directions for columns in order by clause.

**Anti-pattern**

.. code-block:: sql

    SELECT
        a, b
    FROM foo
    ORDER BY a, b DESC

**Best practice**

If any columns in the ``ORDER BY`` clause specify ``ASC`` or ``DESC``, they should
all do so.

.. code-block:: sql

    SELECT
        a, b
    FROM foo
    ORDER BY a ASC, b DESC
