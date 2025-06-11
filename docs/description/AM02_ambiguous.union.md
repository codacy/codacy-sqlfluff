# AM02_ambiguous.union

``UNION [DISTINCT|ALL]`` is preferred over just ``UNION``.

.. note::
   This rule is only enabled for dialects that support ``UNION`` and
   ``UNION DISTINCT`` (``ansi``, ``bigquery``, ``clickhouse``,
   ``databricks``, ``db2``, ``hive``, ``mysql``, ``redshift``,
   ``snowflake``, and ``trino``).

**Anti-pattern**

In this example, ``UNION DISTINCT`` should be preferred over ``UNION``, because
explicit is better than implicit.

.. code-block:: sql

    SELECT a, b FROM table_1
    UNION
    SELECT a, b FROM table_2

**Best practice**

Specify ``DISTINCT`` or ``ALL`` after ``UNION`` (note that ``DISTINCT`` is the
default behavior).

.. code-block:: sql

    SELECT a, b FROM table_1
    UNION DISTINCT
    SELECT a, b FROM table_2
