# AL01_aliasing.table

Implicit/explicit aliasing of table.

Aliasing of table to follow preference
(requiring an explicit ``AS`` is the default).

**Anti-pattern**

In this example, the alias ``voo`` is implicit.

.. code-block:: sql

    SELECT
        voo.a
    FROM foo voo

**Best practice**

Add ``AS`` to make it explicit.

.. code-block:: sql

    SELECT
        voo.a
    FROM foo AS voo
