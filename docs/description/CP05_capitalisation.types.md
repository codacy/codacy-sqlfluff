# CP05_capitalisation.types

Inconsistent capitalisation of datatypes.

**Anti-pattern**

In this example, ``int`` and ``unsigned`` are in lower-case whereas
``VARCHAR`` is in upper-case.

.. code-block:: sql

    CREATE TABLE t (
        a int unsigned,
        b VARCHAR(15)
    );

**Best practice**

Ensure all datatypes are consistently upper or lower case

.. code-block:: sql

    CREATE TABLE t (
        a INT UNSIGNED,
        b VARCHAR(15)
    );
