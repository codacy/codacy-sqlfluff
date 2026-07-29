# PG02_postgres.not_valid_foreign_key

Create PostgreSQL foreign keys as ``NOT VALID`` before validating.

Adding a foreign key constraint normally validates existing rows as part of
the ``ALTER TABLE`` statement. On large tables, this can hold locks for
longer than necessary. Creating the constraint as ``NOT VALID`` defers that
scan so it can be run later with ``VALIDATE CONSTRAINT``.

This rule only applies to the ``postgres`` dialect and is disabled by
default. Enable it with the ``force_enable = True`` flag.

**Anti-pattern**

A foreign key constraint that validates existing rows during creation.

.. code-block:: sql

    ALTER TABLE foo ADD CONSTRAINT fk_bar
        FOREIGN KEY (bar_id) REFERENCES bar (id);

**Best practice**

Create the foreign key as ``NOT VALID``, then validate it in a separate
statement.

.. code-block:: sql

    ALTER TABLE foo ADD CONSTRAINT fk_bar
        FOREIGN KEY (bar_id) REFERENCES bar (id) NOT VALID;

    ALTER TABLE foo VALIDATE CONSTRAINT fk_bar;
