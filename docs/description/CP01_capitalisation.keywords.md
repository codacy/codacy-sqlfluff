# CP01_capitalisation.keywords

Inconsistent capitalisation of keywords.

**Anti-pattern**

In this example, ``select`` is in lower-case whereas ``FROM`` is in upper-case.

.. code-block:: sql

    select
        a
    FROM foo

**Best practice**

Make all keywords either in upper-case or in lower-case.

.. code-block:: sql

    SELECT
        a
    FROM foo

    -- Also good

    select
        a
    from foo
