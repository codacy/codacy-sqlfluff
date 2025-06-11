# CV10_convention.quoted_literals

Consistent usage of preferred quotes for quoted literals.

Some databases allow quoted literals to use either single or double quotes.
Prefer one type of quotes as specified in rule setting, falling back to
alternate quotes to reduce the need for escapes.

Dollar-quoted raw strings are excluded from this rule, as they are mostly used for
literal UDF Body definitions.

.. note::
   This rule only checks quoted literals and not quoted identifiers as they often
   cannot interchange single and double quotes

   This rule is only enabled for dialects that allow single *and* double quotes for
   quoted literals
   (currently ``bigquery``, ``databricks``, ``hive``, ``mysql``, ``sparksql``).
   It can be enabled for other dialects with the ``force_enable = True`` flag.

**Anti-pattern**

.. code-block:: sql
   :force:

    select
        "abc",
        'abc',
        "\"",
        "abc" = 'abc'
    from foo

**Best practice**

Ensure all quoted literals use preferred quotes, unless escaping can be reduced by
using alternate quotes.

.. code-block:: sql
   :force:

    select
        "abc",
        "abc",
        '"',
        "abc" = "abc"
    from foo
