# ST06_structure.column_order

Select wildcards then simple targets before calculations and aggregates.

**Anti-pattern**

.. code-block:: sql

    select
        a,
        *,
        row_number() over (partition by id order by date) as y,
        b
    from x


**Best practice**

Order ``select`` targets in ascending complexity

.. code-block:: sql

    select
        *,
        a,
        b,
        row_number() over (partition by id order by date) as y
    from x
