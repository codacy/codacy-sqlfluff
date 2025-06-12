# LT03_layout.operators

Operators should follow a standard for being before/after newlines.

The configuration for whether operators should be ``trailing`` or
``leading`` is part of :ref:`layoutconfig`. The default configuration is:

.. code-block:: cfg

    [sqlfluff:layout:type:binary_operator]
    line_position = leading

    [sqlfluff:layout:type:comparison_operator]
    line_position = leading

**Anti-pattern**

In this example, if ``line_position = leading`` (or unspecified, as is the
default), then the operator ``+`` should not be at the end of the second line.

.. code-block:: sql

    SELECT
        a +
        b
    FROM foo


**Best practice**

If ``line_position = leading`` (or unspecified, as this is the default),
place the operator after the newline.

.. code-block:: sql

    SELECT
        a
        + b
    FROM foo

If ``line_position = trailing``, place the operator before the newline.

.. code-block:: sql

    SELECT
        a +
        b
    FROM foo
