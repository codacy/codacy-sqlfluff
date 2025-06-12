# RF01_references.from

References cannot reference objects not present in ``FROM`` clause.

.. note::

   This rule is disabled by default for Athena, BigQuery, Databricks, DuckDB, Hive,
   Redshift, SOQL and SparkSQL due to the support of things like
   structs and lateral views which trigger false positives. It can be
   enabled with the ``force_enable = True`` flag.

**Anti-pattern**

In this example, the reference ``vee`` has not been declared.

.. code-block:: sql

    SELECT
        vee.a
    FROM foo

**Best practice**

Remove the reference.

.. code-block:: sql

    SELECT
        a
    FROM foo
