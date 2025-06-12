# ST01_structure.else_null

Do not specify ``else null`` in a case when statement (redundant).

**Anti-pattern**

.. code-block:: sql

    select
        case
            when name like '%cat%' then 'meow'
            when name like '%dog%' then 'woof'
            else null
        end
    from x

**Best practice**

Omit ``else null``

.. code-block:: sql

    select
        case
            when name like '%cat%' then 'meow'
            when name like '%dog%' then 'woof'
        end
    from x
