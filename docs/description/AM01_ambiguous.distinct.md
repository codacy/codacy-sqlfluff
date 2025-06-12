# AM01_ambiguous.distinct

Ambiguous use of ``DISTINCT`` in a ``SELECT`` statement with ``GROUP BY``.

When using ``GROUP BY`` a `DISTINCT`` clause should not be necessary as every
non-distinct ``SELECT`` clause must be included in the ``GROUP BY`` clause.

**Anti-pattern**

``DISTINCT`` and ``GROUP BY`` are conflicting.

.. code-block:: sql

    SELECT DISTINCT
        a
    FROM foo
    GROUP BY a

**Best practice**

Remove ``DISTINCT`` or ``GROUP BY``. In our case, removing ``GROUP BY`` is better.

.. code-block:: sql

    SELECT DISTINCT
        a
    FROM foo
