# AM05_ambiguous.join

Join clauses should be fully qualified.

By default this rule is configured to enforce fully qualified ``INNER JOIN``
clauses, but not ``[LEFT/RIGHT/FULL] OUTER JOIN``. If you prefer a stricter
lint then this is configurable.

**Anti-pattern**

A join is used without specifying the **kind** of join.

.. code-block:: sql
   :force:

    SELECT
        foo
    FROM bar
    JOIN baz;

**Best practice**

Use ``INNER JOIN`` rather than ``JOIN``.

.. code-block:: sql
   :force:

    SELECT
        foo
    FROM bar
    INNER JOIN baz;
