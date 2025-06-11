# CP03_capitalisation.functions

Inconsistent capitalisation of function names.

**Anti-pattern**

In this example, the two ``SUM`` functions don't have the same capitalisation.

.. code-block:: sql

    SELECT
        sum(a) AS aa,
        SUM(b) AS bb
    FROM foo

**Best practice**

Make the case consistent.

.. code-block:: sql

    SELECT
        sum(a) AS aa,
        sum(b) AS bb
    FROM foo
