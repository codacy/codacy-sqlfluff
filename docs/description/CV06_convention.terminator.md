# CV06_convention.terminator

Statements must end with a semi-colon.

**Anti-pattern**

A statement is not immediately terminated with a semi-colon. The ``•`` represents
space.

.. code-block:: sql
   :force:

    SELECT
        a
    FROM foo

    ;

    SELECT
        b
    FROM bar••;

**Best practice**

Immediately terminate the statement with a semi-colon.

.. code-block:: sql
   :force:

    SELECT
        a
    FROM foo;
