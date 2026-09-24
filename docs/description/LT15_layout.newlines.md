# LT15_layout.newlines

Too many consecutive blank lines.

**Anti-pattern**

In this example, the maximum number of empty lines inside a statement is set to 0.

.. code-block:: sql

    SELECT 'a' AS col
    FROM tab


    WHERE x = 4
    ORDER BY y


    LIMIT 5
    ;

**Best practice**

.. code-block:: sql

    SELECT 'a' AS col
    FROM tab
    WHERE x = 4
    ORDER BY y
    LIMIT 5
    ;

A minimum can also be required between statements. With
``minimum_empty_lines_between_statements = 1``, this is an anti-pattern:

.. code-block:: sql

    SELECT a FROM tab;
    SELECT b FROM tab;

and this is the best practice:

.. code-block:: sql

    SELECT a FROM tab;

    SELECT b FROM tab;

The minimum defaults to ``0``, which leaves the rule's existing behaviour
unchanged. It applies only between statements, never inside one or between
batches, matching the scope its name describes.

.. note::

    ``minimum_empty_lines_between_statements`` is capped by
    ``maximum_empty_lines_between_statements``. The two settings validate
    independently, so a minimum above the maximum is accepted configuration,
    but no file can satisfy both: the minimum inserts blank lines and the
    maximum deletes them straight back, so ``sqlfluff fix`` alternates
    between the two results on every run instead of converging. Where the
    cap changes what would otherwise be reported, a warning is emitted
    naming both values.
