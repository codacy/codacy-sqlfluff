# CV09_convention.blocked_words

Block a list of configurable words from being used.

This generic rule can be useful to prevent certain keywords, functions, or objects
from being used. Only whole words can be blocked, not phrases, nor parts of words.

This block list is case insensitive.

**Example use cases**

* We prefer ``BOOL`` over ``BOOLEAN`` and there is no existing rule to enforce
  this. Until such a rule is written, we can add ``BOOLEAN`` to the deny list
  to cause a linting error to flag this.
* We have deprecated a schema/table/function and want to prevent it being used
  in future. We can add that to the denylist and then add a ``-- noqa: CV09`` for
  the few exceptions that still need to be in the code base for now.

**Anti-pattern**

If the ``blocked_words`` config is set to ``deprecated_table,bool`` then the
following will flag:

.. code-block:: sql

    SELECT * FROM deprecated_table WHERE 1 = 1;
    CREATE TABLE myschema.t1 (a BOOL);

**Best practice**

Do not used any blocked words:

.. code-block:: sql

    SELECT * FROM another_table WHERE 1 = 1;
    CREATE TABLE myschema.t1 (a BOOLEAN);
