# CV08_convention.left_join

Use ``LEFT JOIN`` instead of ``RIGHT JOIN``.

**Anti-pattern**

``RIGHT JOIN`` is used.

.. code-block:: sql
   :force:

    SELECT
        foo.col1,
        bar.col2
    FROM foo
    RIGHT JOIN bar
        ON foo.bar_id = bar.id;

**Best practice**

Refactor and use ``LEFT JOIN`` instead.

.. code-block:: sql
   :force:

    SELECT
        foo.col1,
        bar.col2
    FROM bar
    LEFT JOIN foo
        ON foo.bar_id = bar.id;
