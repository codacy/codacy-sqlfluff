# AL09_aliasing.self_alias.column

Column aliases should not alias to itself, i.e. self-alias.

Renaming the column to itself is a redundant piece of SQL,
which doesn't affect its functionality. This rule only applies
when aliasing to an exact copy of the column reference (e.g.
:code:`foo as foo` or :code:`"BAR" as "BAR"`, see note below on
more complex examples). Aliases which effectively change the casing of
an identifier are still allowed.

.. note::

   This rule works in conjunction with :sqlfluff:ref:`references.quoting`
   (:sqlfluff:ref:`RF06`) and :sqlfluff:ref:`capitalisation.identifiers`
   (:sqlfluff:ref:`CP02`) to handle self aliases with mixed quoting
   and casing. In the situation that these two rules are not enabled
   then this rule will only fix the strict case where the quoting
   and casing of the alias and reference are the same.

   If those two rules are enabled, the fixes applied may result in a
   situation where this rule can kick in as a secondary effect. For
   example this :ref:`snowflake_dialect_ref` query:

   .. code-block:: sql

      -- Original Query. AL09 will not trigger because casing and
      -- quoting are different. RF06 will however fix the unnecessary
      -- quoting of "COL".
      SELECT "COL" AS col FROM table;
      -- After RF06, the query will look like this, at which point
      -- CP02 will see the inconsistent capitalisation. Depending
      -- on the configuration it will change one of the identifiers.
      -- Let's assume the default configuration of "consistent".
      SELECT COL AS col FROM table;
      -- After CP02, the alias and the reference will be the same
      -- and at this point AL09 can take over and remove the alias.
      SELECT COL AS COL FROM table;
      -- ..resulting in:
      SELECT COL FROM table;

   This interdependence between the rules, and the configuration
   options offered by each one means a variety of outcomes can be
   achieved by enabling and disabling each one. See
   :ref:`ruleselection` and :ref:`ruleconfig` for more details.

**Anti-pattern**

Aliasing the column to itself, where not necessary for changing the case
of an identifier.

.. code-block:: sql

    SELECT
        col AS col,
        "Col" AS "Col",
        COL AS col
    FROM table;

**Best practice**

Not to use alias to rename the column to its original name.
Self-aliasing leads to redundant code without changing any functionality,
unless used to effectively change the case of the identifier.

.. code-block:: sql

    SELECT
        col,
        "Col"
        COL,
    FROM table;

    -- Re-casing aliasing is still allowed where necessary, i.e.
    SELECT
        col as "Col",
        "col" as "COL"
    FROM table;
