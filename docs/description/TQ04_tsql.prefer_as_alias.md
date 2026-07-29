# TQ04_tsql.prefer_as_alias

Prefer ANSI-style ``AS`` aliasing over ``alias = expression`` in T-SQL.

T-SQL supports an alternative alias form in ``SELECT`` clauses using
``alias = expression``. This rule enforces the more ANSI-style
``expression AS alias`` form instead.

This rule only applies to the ``tsql`` dialect and is disabled by
default. Enable it with the ``force_enable = True`` flag.

**Anti-pattern**

.. code-block:: sql
   :force:

    SELECT
        help3 = 'hello',
        help4 = CASE WHEN help = 'apple' THEN 'hello' END

**Best practice**

.. code-block:: sql
   :force:

    SELECT
        'hello' AS help3,
        CASE WHEN help = 'apple' THEN 'hello' END AS help4
