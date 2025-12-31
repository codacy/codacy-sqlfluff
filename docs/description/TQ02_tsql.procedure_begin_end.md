# TQ02_tsql.procedure_begin_end

Procedure bodies with multiple statements should be wrapped in BEGIN/END.

**Anti-pattern**

Procedure bodies with multiple statements should be wrapped in BEGIN/END
for clarity and consistency.

.. code-block:: sql
   :force:

    CREATE PROCEDURE Reporting.MultipleStatements
    AS
    SELECT
        [ID],
        [DataDate],
        [CaseOutput]
    FROM Table1;

    SELECT
        [ID],
        [DataDate],
        [CaseOutput]
    FROM Table2;

**Best practice**

Wrap procedure bodies with multiple statements in BEGIN/END blocks.

.. code-block:: sql
   :force:

    CREATE PROCEDURE Reporting.MultipleStatements
    AS
    BEGIN
        SELECT
            [ID],
            [DataDate],
            [CaseOutput]
        FROM Table1;

        SELECT
            [ID],
            [DataDate],
            [CaseOutput]
        FROM Table2;
    END
