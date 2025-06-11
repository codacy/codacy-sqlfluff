# AL05_aliasing.unused

Tables should not be aliased if that alias is not used.

**Anti-pattern**

.. code-block:: sql

    SELECT
        a
    FROM foo AS zoo

**Best practice**

Use the alias or remove it. An unused alias makes code
harder to read without changing any functionality.

.. code-block:: sql

    SELECT
        zoo.a
    FROM foo AS zoo

    -- Alternatively...

    SELECT
        a
    FROM foo
