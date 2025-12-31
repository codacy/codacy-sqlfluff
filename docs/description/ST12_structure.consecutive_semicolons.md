# ST12_structure.consecutive_semicolons

Consecutive semicolons detected.

This rule flags runs of two or more semicolons (optionally with intervening
whitespace/newlines) which usually indicate an empty statement or an
accidental duplicate terminator.

**Anti-pattern**

.. code-block:: sql
   :force:

    SELECT 1;;
    ;;SELECT 2;

**Best practice**

Collapse duplicate semicolons unless intentionally separating batches.

.. code-block:: sql
   :force:

    SELECT 1;
    SELECT 2;
