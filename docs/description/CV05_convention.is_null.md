# CV05_convention.is_null

Comparisons with NULL should use "IS" or "IS NOT".

**Anti-pattern**

In this example, the ``=`` operator is used to check for ``NULL`` values.

.. code-block:: sql

    SELECT
        a
    FROM foo
    WHERE a = NULL


**Best practice**

Use ``IS`` or ``IS NOT`` to check for ``NULL`` values.

.. code-block:: sql

    SELECT
        a
    FROM foo
    WHERE a IS NULL
