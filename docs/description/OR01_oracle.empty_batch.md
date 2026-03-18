# OR01_oracle.empty_batch

Remove empty batches.

**Anti-pattern**

Empty batches (containing only / statements) should be removed.

.. code-block:: sql
   :force:

    SELECT 1 FROM DUAL;

    /

    /

**Best practice**

Remove empty batches.

.. code-block:: sql
   :force:

    SELECT 1 FROM DUAL;

    /
