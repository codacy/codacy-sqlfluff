# CV13_convention.last_select_star

The final ``SELECT`` of a CTE model should be ``SELECT * FROM ...``.

This is a convention popularised by the dbt
`style guide
<https://docs.getdbt.com/best-practices/how-we-style/0-how-we-style-our-dbt-projects>`_,
where the final statement of a model is a "passthrough" select from the last
CTE. Keeping the final select as ``SELECT * FROM final`` makes a model easier
to debug, because the source of the final result set can be swapped by
changing a single line (for example replacing ``final`` with an earlier CTE).

To avoid flagging ad-hoc queries, this rule only applies when the *last*
top-level statement of a file is a ``WITH ... SELECT`` (i.e. it uses CTEs).
Plain ``SELECT`` statements, and files ending in DML or DDL, are not in
scope. The final select must also be a pure passthrough: a lone
``SELECT * FROM <cte>`` with no further transformation (``WHERE``,
``GROUP BY``, ``DISTINCT``, ``ORDER BY``, ``LIMIT``, etc.).

This convention is opinionated and not universally agreed upon, so this
rule is **disabled by default**. It can be enabled with the
``force_enable = True`` flag:

.. code-block:: cfg

    [sqlfluff:rules:convention.last_select_star]
    force_enable = True

**Anti-pattern**

The final select of a CTE model lists explicit columns rather than selecting
everything from the final CTE.

.. code-block:: sql

    WITH final AS (
        SELECT
            a,
            b
        FROM foo
    )

    SELECT
        a,
        b
    FROM final

**Best practice**

Select everything from the final CTE.

.. code-block:: sql

    WITH final AS (
        SELECT
            a,
            b
        FROM foo
    )

    SELECT * FROM final
