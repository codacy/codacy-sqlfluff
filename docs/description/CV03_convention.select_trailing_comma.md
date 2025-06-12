# CV03_convention.select_trailing_comma

Trailing commas within select clause.

.. note::
   For many database backends this is allowed. For some users
   this may be something they wish to enforce (in line with
   Python best practice). Many database backends regard this
   as a syntax error, and as such the `SQLFluff` default is to
   forbid trailing commas in the select clause.

**Anti-pattern**

.. code-block:: sql

    SELECT
        a,
        b,
    FROM foo

**Best practice**

.. code-block:: sql

    SELECT
        a,
        b
    FROM foo
