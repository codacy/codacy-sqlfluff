# AL02_aliasing.column

Implicit/explicit aliasing of columns.

Aliasing of columns to follow preference
(explicit using an ``AS`` clause is default).

**Anti-pattern**

In this example, the alias for column ``a`` is implicit.

.. code-block:: sql

    SELECT
        a alias_col
    FROM foo

**Best practice**

Add ``AS`` to make it explicit.

.. code-block:: sql

    SELECT
        a AS alias_col
    FROM foo
