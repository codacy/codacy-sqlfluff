# RF06_references.quoting

Unnecessary quoted identifier.

This rule will fail if the quotes used to quote an identifier are (un)necessary
depending on the ``force_quote_identifier`` configuration. This rule applies to
both column *references* and their *aliases*. The *default* (safe) behaviour is
designed not to unexpectedly corrupt SQL. That means the circumstances in which
quotes can be safely removed depends on the current dialect would resolve the
unquoted variant of the identifier (see below for examples).

Additionally this rule may be configured to a more aggressive setting by setting
:code:`case_sensitive` to :code:`False`, in which case quotes will be removed
regardless of the casing of the contained identifier. Any identifiers which contain
special characters, spaces or keywords will still be left quoted. This setting is
more appropriate for projects or teams where there is more control over the inputs
and outputs of queries, and where it's more viable to institute rules such
as enforcing that all identifiers are the default casing (and therefore meaning
that using quotes to change the case of identifiers is unnecessary).

.. list-table::
   :widths: 26 26 48
   :header-rows: 1

   * - Dialect group
     - ✅ Example where quotes are safe to remove.
     - ⚠️ Examples where quotes are not safe to remove.
   * - Natively :code:`UPPERCASE` dialects e.g. Snowflake, BigQuery,
       TSQL & Oracle.
     - Identifiers which, without quotes, would resolve to the default
       casing of :code:`FOO` i.e. :code:`"FOO"`.
     - Identifiers where the quotes are necessary to preserve case
       (e.g. :code:`"Foo"` or :code:`"foo"`), or where the identifier
       contains something invalid without the quotes such as keywords
       or special characters e.g. :code:`"SELECT"`, :code:`"With Space"`
       or :code:`"Special&Characters"`.
   * - Natively :code:`lowercase` dialects e.g. Athena,
       Hive & Postgres
     - Identifiers which, without quotes, would resolve to the default
       casing of :code:`foo` i.e. :code:`"foo"`.
     - Identifiers where the quotes are necessary to preserve case
       (e.g. :code:`"Foo"` or :code:`"foo"`), or where the identifier
       contains something invalid without the quotes such as keywords
       or special characters e.g. :code:`"SELECT"`, :code:`"With Space"`
       or :code:`"Special&Characters"`.
   * - Case insensitive dialects e.g. :ref:`duckdb_dialect_ref` or
       :ref:`sparksql_dialect_ref`
     - Any identifiers which are valid without quotes: e.g. :code:`"FOO"`,
       :code:`"foo"`, :code:`"Foo"`, :code:`"fOo"`, :code:`FOO` and
       :code:`foo` would all resolve to the same object.
     - Identifiers which contain something invalid without the quotes
       such as keywords or special characters e.g. :code:`"SELECT"`,
       :code:`"With Space"` or :code:`"Special&Characters"`.

This rule is closely associated with (and constrained by the same above
factors) as :sqlfluff:ref:`aliasing.self_alias.column` (:sqlfluff:ref:`AL09`).

When ``prefer_quoted_identifiers = False`` (default behaviour), the quotes are
unnecessary, except for reserved keywords and special characters in identifiers.

**Anti-pattern**

In this example, valid unquoted identifiers,
that are not also reserved keywords, are needlessly quoted.

.. code-block:: sql

    SELECT "foo" as "bar";  -- For lowercase dialects like Postgres
    SELECT "FOO" as "BAR";  -- For uppercase dialects like Snowflake

**Best practice**

Use unquoted identifiers where possible.

.. code-block:: sql

    SELECT foo as bar;  -- For lowercase dialects like Postgres
    SELECT FOO as BAR;  -- For uppercase dialects like Snowflake

    -- Note that where the case of the quoted identifier requires
    -- the quotes to remain, or where the identifier cannot be
    -- unquoted because it would be invalid to do so, the quotes
    -- may remain. For example:
    SELECT
        "Case_Sensitive_Identifier" as is_allowed,
        "Identifier with spaces or speci@l characters" as this_too,
        "SELECT" as also_reserved_words
    FROM "My Table With Spaces"

When ``prefer_quoted_identifiers = True``, the quotes are always necessary, no
matter if the identifier is valid, a reserved keyword, or contains special
characters.

.. note::
   Note due to different quotes being used by different dialects supported by
   `SQLFluff`, and those quotes meaning different things in different contexts,
   this mode is not ``sqlfluff fix`` compatible.

**Anti-pattern**

In this example, a valid unquoted identifier, that is also not a reserved keyword,
is required to be quoted.

.. code-block:: sql

    SELECT 123 as foo

**Best practice**
Use quoted identifiers.

.. code-block:: sql

    SELECT 123 as "foo" -- For ANSI, ...
    -- or
    SELECT 123 as `foo` -- For BigQuery, MySql, ...
