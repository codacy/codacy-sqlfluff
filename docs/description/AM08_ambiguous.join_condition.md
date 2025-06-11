# AM08_ambiguous.join_condition

Implicit cross join detected.

**Anti-pattern**

Cross joins are valid, but rare in the wild - and more often created by mistake
than on purpose. This rule catches situations where a cross join has been specified,
but not explicitly and so the risk of a mistaken cross join is highly likely.

.. code-block:: sql
   :force:

    SELECT
        foo
    FROM bar
    JOIN baz;

**Best practice**

Use CROSS JOIN.

.. code-block:: sql
   :force:

    SELECT
        foo
    FROM bar
    CROSS JOIN baz;
