# LT13_layout.start_of_file

Files must not begin with newlines or whitespace.

**Anti-pattern**

The file begins with newlines or whitespace. The ``^``
represents the beginning of the file.

.. code-block:: sql
   :force:

    ^

    SELECT
        a
    FROM foo

    -- Beginning on an indented line is also forbidden,
    -- (the • represents space).

    ••••SELECT
    ••••a
    FROM
    ••••foo

**Best practice**

Start file on either code or comment. (The ``^`` represents the beginning
of the file.)

.. code-block:: sql
   :force:


    ^SELECT
        a
    FROM foo

    -- Including an initial block comment.

    ^/*
    This is a description of my SQL code.
    */
    SELECT
        a
    FROM
        foo

    -- Including an initial inline comment.

    ^--This is a description of my SQL code.
    SELECT
        a
    FROM
        foo
