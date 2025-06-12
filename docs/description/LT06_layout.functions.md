# LT06_layout.functions

Function name not immediately followed by parenthesis.

**Anti-pattern**

In this example, there is a space between the function and the parenthesis.

.. code-block:: sql

    SELECT
        sum (a)
    FROM foo

**Best practice**

Remove the space between the function and the parenthesis.

.. code-block:: sql

    SELECT
        sum(a)
    FROM foo
