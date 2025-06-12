# RF05_references.special_chars

Do not use special characters in identifiers.

**Anti-pattern**

Using special characters within identifiers when creating or aliasing objects.

.. code-block:: sql

    CREATE TABLE DBO.ColumnNames
    (
        [Internal Space] INT,
        [Greater>Than] INT,
        [Less<Than] INT,
        Number# INT
    )

**Best practice**

Identifiers should include only alphanumerics and underscores.

.. code-block:: sql

    CREATE TABLE DBO.ColumnNames
    (
        [Internal_Space] INT,
        [GreaterThan] INT,
        [LessThan] INT,
        NumberVal INT
    )
