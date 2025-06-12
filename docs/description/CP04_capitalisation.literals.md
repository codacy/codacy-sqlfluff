# CP04_capitalisation.literals

Inconsistent capitalisation of boolean/null literal.

**Anti-pattern**

In this example, ``null`` and ``false`` are in lower-case whereas ``TRUE`` is in
upper-case.

.. code-block:: sql

    select
        a,
        null,
        TRUE,
        false
    from foo

**Best practice**

Ensure all literal ``null``/``true``/``false`` literals are consistently
upper or lower case

.. code-block:: sql

    select
        a,
        NULL,
        TRUE,
        FALSE
    from foo

    -- Also good

    select
        a,
        null,
        true,
        false
    from foo
