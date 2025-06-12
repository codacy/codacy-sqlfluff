# AL03_aliasing.expression

Column expression without alias. Use explicit `AS` clause.

**Anti-pattern**

In this example, there is no alias for both sums.

.. code-block:: sql

    SELECT
        sum(a),
        sum(b)
    FROM foo

**Best practice**

Add aliases.

.. code-block:: sql

    SELECT
        sum(a) AS a_sum,
        sum(b) AS b_sum
    FROM foo
