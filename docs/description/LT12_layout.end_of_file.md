# LT12_layout.end_of_file

Files must end with a single trailing newline.

**Anti-pattern**

The content in file does not end with a single trailing newline. The ``$``
represents end of file.

.. code-block:: sql
   :force:

    SELECT
        a
    FROM foo$

    -- Ending on an indented line means there is no newline
    -- at the end of the file, the • represents space.

    SELECT
    ••••a
    FROM
    ••••foo
    ••••$

    -- Ending on a semi-colon means the last line is not a
    -- newline.

    SELECT
        a
    FROM foo
    ;$

    -- Ending with multiple newlines.

    SELECT
        a
    FROM foo

    $

**Best practice**

Add trailing newline to the end. The ``$`` character represents end of file.

.. code-block:: sql
   :force:

    SELECT
        a
    FROM foo
    $

    -- Ensuring the last line is not indented so is just a
    -- newline.

    SELECT
    ••••a
    FROM
    ••••foo
    $

    -- Even when ending on a semi-colon, ensure there is a
    -- newline after.

    SELECT
        a
    FROM foo
    ;
    $
