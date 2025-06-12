# LT07_layout.cte_bracket

``WITH`` clause closing bracket should be on a new line.

**Anti-pattern**

In this example, the closing bracket is on the same line as CTE.

.. code-block:: sql
   :force:

    WITH zoo AS (
        SELECT a FROM foo)

    SELECT * FROM zoo

**Best practice**

Move the closing bracket on a new line.

.. code-block:: sql

    WITH zoo AS (
        SELECT a FROM foo
    )

    SELECT * FROM zoo
