# CV07_convention.statement_brackets

Top-level statements should not be wrapped in brackets.

**Anti-pattern**

A top-level statement is wrapped in brackets.

.. code-block:: sql
   :force:

    (SELECT
        foo
    FROM bar)

    -- This also applies to statements containing a sub-query.

    (SELECT
        foo
    FROM (SELECT * FROM bar))

**Best practice**

Don't wrap top-level statements in brackets.

.. code-block:: sql
   :force:

    SELECT
        foo
    FROM bar

    -- Likewise for statements containing a sub-query.

    SELECT
        foo
    FROM (SELECT * FROM bar)
