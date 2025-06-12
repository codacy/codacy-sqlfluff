# CV01_convention.not_equal

Consistent usage of ``!=`` or ``<>`` for "not equal to" operator.

**Anti-pattern**

.. code-block:: sql

    SELECT * FROM X WHERE 1 <> 2 AND 3 != 4;

**Best practice**

Ensure all "not equal to" comparisons are consistent, not mixing ``!=`` and ``<>``.

.. code-block:: sql

    SELECT * FROM X WHERE 1 != 2 AND 3 != 4;
