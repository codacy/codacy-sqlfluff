# RF02_references.qualification

References should be qualified if select has more than one referenced table/view.

.. note::
   Except if they're present in a ``USING`` clause.

**Anti-pattern**

In this example, the reference ``vee`` has not been declared,
and the variables ``a`` and ``b`` are potentially ambiguous.

.. code-block:: sql

    SELECT a, b
    FROM foo
    LEFT JOIN vee ON vee.a = foo.a

**Best practice**

Add the references.

.. code-block:: sql

    SELECT foo.a, vee.b
    FROM foo
    LEFT JOIN vee ON vee.a = foo.a
