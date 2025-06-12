# LT01_layout.spacing

Inappropriate Spacing.

This rule checks for an enforces the spacing as configured in
:ref:`layoutconfig`. This includes excessive whitespace,
trailing whitespace at the end of a line and also the wrong
spacing between elements on the line. Because of this wide reach
you may find that you wish to add specific configuration in your
project to tweak how specific elements are treated. Rather than
configuration on this specific rule, use the `sqlfluff.layout`
section of your configuration file to customise how this rule
operates.

The ``•`` character represents a space in the examples below.

**Anti-pattern**

.. code-block:: sql
    :force:

    SELECT
        a,        b(c) as d••
    FROM foo••••
    JOIN bar USING(a)

**Best practice**

* Unless an indent or preceding a comment, whitespace should
  be a single space.

* There should also be no trailing whitespace at the ends of lines.

* There should be a space after :code:`USING` so that it's not confused
  for a function.

.. code-block:: sql

    SELECT
        a, b(c) as d
    FROM foo
    JOIN bar USING (a)
