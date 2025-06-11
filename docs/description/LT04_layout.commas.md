# LT04_layout.commas

Leading/Trailing comma enforcement.

The configuration for whether operators should be ``trailing`` or
``leading`` is part of :ref:`layoutconfig`. The default configuration is:

.. code-block:: cfg

    [sqlfluff:layout:type:comma]
    line_position = trailing

**Anti-pattern**

There is a mixture of leading and trailing commas.

.. code-block:: sql

    SELECT
        a
        , b,
        c
    FROM foo

**Best practice**

By default, `SQLFluff` prefers trailing commas. However it
is configurable for leading commas. The chosen style must be used
consistently throughout your SQL.

.. code-block:: sql

    SELECT
        a,
        b,
        c
    FROM foo

    -- Alternatively, set the configuration file to 'leading'
    -- and then the following would be acceptable:

    SELECT
        a
        , b
        , c
    FROM foo
