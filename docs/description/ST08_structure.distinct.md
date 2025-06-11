# ST08_structure.distinct

``DISTINCT`` used with parentheses.

**Anti-pattern**

In this example, parentheses are not needed and confuse
``DISTINCT`` with a function. The parentheses can also be misleading
about which columns are affected by the ``DISTINCT`` (all the columns!).

.. code-block:: sql

    SELECT DISTINCT(a), b FROM foo

**Best practice**

Remove parentheses to be clear that the ``DISTINCT`` applies to
both columns.

.. code-block:: sql

    SELECT DISTINCT a, b FROM foo
