# TQ03_tsql.empty_batch

Remove empty batches.

**Anti-pattern**

Empty batches (containing only GO statements) should be removed.

.. code-block:: sql
   :force:

    CREATE TABLE dbo.test (
        testcol1 INT NOT NULL,
        testcol2 INT NOT NULL
    );

    GO

    GO

**Best practice**

Remove empty batches.

.. code-block:: sql
   :force:

    CREATE TABLE dbo.test (
        testcol1 INT NOT NULL,
        testcol2 INT NOT NULL
    );

    GO
