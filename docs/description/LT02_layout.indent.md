# LT02_layout.indent

Incorrect Indentation.

**Anti-pattern**

The ``•`` character represents a space and the ``→`` character represents a tab.
In this example, the third line contains five spaces instead of four and
the second line contains two spaces and one tab.

.. code-block:: sql
   :force:

    SELECT
    ••→a,
    •••••b
    FROM foo


**Best practice**

Change the indentation to use a multiple of four spaces. This example also
assumes that the ``indent_unit`` config value is set to ``space``. If it
had instead been set to ``tab``, then the indents would be tabs instead.

.. code-block:: sql
   :force:

    SELECT
    ••••a,
    ••••b
    FROM foo
