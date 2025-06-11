# RF03_references.consistent

Column references should be qualified consistently in single table statements.

.. note::
    For BigQuery, Hive and Redshift this rule is disabled by default.
    This is due to historical false positives associated with STRUCT data types.
    This default behaviour may be changed in the future.
    The rule can be enabled with the ``force_enable = True`` flag.

"consistent" will be fixed to "qualified" if inconsistency is found.

**Anti-pattern**

In this example, only the reference to ``b`` is qualified.

.. code-block:: sql

    SELECT
        a,
        foo.b
    FROM foo

**Best practice**

Either all column references should be qualified, or all unqualified.

.. code-block:: sql

    SELECT
        a,
        b
    FROM foo

    -- Also good

    SELECT
        foo.a,
        foo.b
    FROM foo
