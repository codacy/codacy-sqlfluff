# ST04_structure.nested_case

Nested ``CASE`` statement in ``ELSE`` clause could be flattened.

**Anti-pattern**

In this example, the outer ``CASE``'s ``ELSE`` is an unnecessary, nested ``CASE``.

.. code-block:: sql

    SELECT
      CASE
        WHEN species = 'Cat' THEN 'Meow'
        ELSE
        CASE
           WHEN species = 'Dog' THEN 'Woof'
        END
      END as sound
    FROM mytable

**Best practice**

Move the body of the inner ``CASE`` to the end of the outer one.

.. code-block:: sql

    SELECT
      CASE
        WHEN species = 'Cat' THEN 'Meow'
        WHEN species = 'Dog' THEN 'Woof'
      END AS sound
    FROM mytable
