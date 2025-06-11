# CV11_convention.casting_style

Enforce consistent type casting style.

.. note::
    This is only compatible with 2-arguments CONVERT as
    some dialects allow an optional 3rd argument e.g TSQL,
    which cannot be rewritten into CAST.
    This rule is disabled by default for Teradata because it supports different
    type casting apart from CONVERT and ::
    e.g DATE '2007-01-01', '9999-12-31' (DATE).

**Anti-pattern**

Using mixture of CONVERT, :: and CAST when ``preferred_type_casting_style``
config is set to ``consistent`` (default).

.. code-block:: sql

    SELECT
        CONVERT(int, 1) AS bar,
        100::int::text,
        CAST(10 AS text) AS coo
    FROM foo;

**Best practice**

Use consistent type casting style.

.. code-block:: sql

    SELECT
        CAST(1 AS int) AS bar,
        CAST(CAST(100 AS int) AS text),
        CAST(10 AS text) AS coo
    FROM foo;
