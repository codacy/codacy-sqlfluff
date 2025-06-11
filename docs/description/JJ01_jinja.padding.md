# JJ01_jinja.padding

Jinja tags should have a single whitespace on either side.

This rule is only active if the ``jinja`` templater (or one of it's
subclasses, like the ``dbt`` templater) are used for the current file.

**Anti-pattern**

Jinja tags with either no whitespace or very long whitespace
are hard to read.

.. code-block:: jinja
   :force:

    SELECT {{    a     }} from {{ref('foo')}}

**Best practice**

A single whitespace surrounding Jinja tags, alternatively
longer gaps containing newlines are acceptable.

.. code-block:: jinja
   :force:

    SELECT {{ a }} from {{ ref('foo') }};
    SELECT {{ a }} from {{
        ref('foo')
    }};
