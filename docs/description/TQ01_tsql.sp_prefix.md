# TQ01_tsql.sp_prefix

``SP_`` prefix should not be used for user-defined stored procedures in T-SQL.

**Anti-pattern**

The ``SP_`` prefix is used to identify system procedures and can adversely
affect performance of the user-defined stored procedure. It can also break
system procedures if there is a naming conflict.

.. code-block:: sql
   :force:

    CREATE PROCEDURE dbo.sp_pull_data
    AS
    SELECT
        ID,
        DataDate,
        CaseOutput
    FROM table1

**Best practice**

Use a different name for the stored procedure.

.. code-block:: sql
   :force:

    CREATE PROCEDURE dbo.pull_data
    AS
    SELECT
        ID,
        DataDate,
        CaseOutput
    FROM table1

    -- Alternatively prefix with USP_ to
    -- indicate a user-defined stored procedure.

    CREATE PROCEDURE dbo.usp_pull_data
    AS
    SELECT
        ID,
        DataDate,
        CaseOutput
    FROM table1
