# ST10_structure.constant_expression

Redundant constant expression.

Including an expression that always evaluates to
either ``TRUE`` or ``FALSE`` regardless of the input columns is
unnecessary and makes statements harder to read and understand.

Constant conditions are sometimes mistakes (by mistyping the column
name intended), and sometimes the result of incorrect information that
they are necessary in some circumstances. In the former case, they can
sometimes result in a cartesian join if it was supposed to be a join
condition. Given the ambiguity of intent, this rule does not suggest
an automatic fix, and instead invites the user to resolve the problem
manually.

**Anti-pattern**

.. code-block:: sql

    SELECT *
    FROM my_table
    -- This following WHERE clause is redundant.
    WHERE my_table.col = my_table.col

**Best practice**

.. code-block:: sql

    SELECT *
    FROM my_table
    -- Replace with a condition that includes meaningful logic,
    -- or remove the condition entirely.
    WHERE my_table.col > 3
