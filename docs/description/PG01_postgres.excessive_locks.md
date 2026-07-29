# PG01_postgres.excessive_locks

Avoid excessive locks in PostgreSQL DDL statements.

Several PostgreSQL DDL operations acquire locks that block reads or writes
for the duration of the operation. On large tables this can cause significant
downtime. This rule flags statements that should use safer alternatives:

* ``CREATE INDEX`` → use ``CONCURRENTLY`` (``CREATE UNIQUE INDEX`` excluded)
* ``DROP INDEX`` → use ``CONCURRENTLY``
* ``REINDEX`` → use ``CONCURRENTLY``
* ``REFRESH MATERIALIZED VIEW`` → use ``CONCURRENTLY``

This rule only applies to the ``postgres`` dialect and is disabled by
default. Enable it with the ``force_enable = True`` flag.

**Anti-pattern**

DDL that acquires excessive locks.

.. code-block:: sql

    CREATE INDEX idx_foo ON bar (tenant_id);

    DROP INDEX idx_foo;

    REINDEX INDEX idx_foo;

    REFRESH MATERIALIZED VIEW my_view;

**Best practice**

Use non-blocking alternatives.

.. code-block:: sql

    CREATE INDEX CONCURRENTLY idx_foo ON bar (tenant_id);

    DROP INDEX CONCURRENTLY idx_foo;

    REINDEX INDEX CONCURRENTLY idx_foo;

    REFRESH MATERIALIZED VIEW CONCURRENTLY my_view;
