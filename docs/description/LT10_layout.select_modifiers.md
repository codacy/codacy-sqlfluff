# LT10_layout.select_modifiers

``SELECT`` modifiers (e.g. ``DISTINCT``) must be on the same line as ``SELECT``.

**Anti-pattern**

.. code-block:: sql

    select
        distinct a,
        b
    from x


**Best practice**

.. code-block:: sql

    select distinct
        a,
        b
    from x
