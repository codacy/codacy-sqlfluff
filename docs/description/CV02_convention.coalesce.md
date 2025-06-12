# CV02_convention.coalesce

Use ``COALESCE`` instead of ``IFNULL`` or ``NVL``.

**Anti-pattern**

``IFNULL`` or ``NVL`` are used to fill ``NULL`` values.

.. code-block:: sql

    SELECT ifnull(foo, 0) AS bar,
    FROM baz;

    SELECT nvl(foo, 0) AS bar,
    FROM baz;

**Best practice**

Use ``COALESCE`` instead.
``COALESCE`` is universally supported,
whereas Redshift doesn't support ``IFNULL``
and BigQuery doesn't support ``NVL``.
Additionally, ``COALESCE`` is more flexible
and accepts an arbitrary number of arguments.

.. code-block:: sql

    SELECT coalesce(foo, 0) AS bar,
    FROM baz;
