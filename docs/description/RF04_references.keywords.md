# RF04_references.keywords

Keywords should not be used as identifiers.

Although `unreserved` keywords `can` be used as identifiers,
and `reserved words` can be used as quoted identifiers,
best practice is to avoid where possible, to avoid any
misunderstandings as to what the alias represents.

.. note::
   Note that `reserved` keywords cannot be used as unquoted identifiers
   and will cause parsing errors and so are not covered by this rule.

**Anti-pattern**

In this example, ``SUM`` (built-in function) is used as an alias.

.. code-block:: sql

    SELECT
        sum.a
    FROM foo AS sum

**Best practice**

Avoid keywords as the name of an alias.

.. code-block:: sql

    SELECT
        vee.a
    FROM foo AS vee
