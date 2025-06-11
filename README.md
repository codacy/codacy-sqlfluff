# Codacy SQLFluff

This is the docker engine we use at Codacy to have [SQLFluff](https://docs.sqlfluff.com/en/stable/index.html) support.
You can also create a docker to integrate the tool and language of your choice!
See the [codacy-engine-scala-seed](https://github.com/codacy/codacy-engine-scala-seed) repository for more information.

## Python compatibility
Compatible with Python 3.13


## Dialects compatibility
-  ansi
-  athena
-  bigquery
-  clickhouse
-  databricks
-  db2
-  duckdb
-  exasol
-  greenplum
-  hive
-  impala
-  mariadb
-  materialize
-  mysql
-  oracle
-  postgres
-  redshift
-  snowflake
-  soql
-  sparksql
-  sqlite
-  starrocks
-  teradata
-  trino
-  tsql
-  vertica

## Configuration files supported (it follows the same order)
-  setup.cfg
-  tox.ini
-  pep8.ini
-  .sqlfluff
-  pyproject.toml

## Note
By default we're running SQLFluff with the dialect postgres because the flag is mandatory.
If your codebase is based on another dialect above, please create a simple .sqlfluff config file
in the root of your repository with the following content (let's use oracle as example):

```text
[sqlfluff]
dialect = oracle
```
It will run for all existing rules for the dialect oracle

If you want to ignore some of the rules, please use the same configuration file:

```text
[sqlfluff]
dialect = postgres
exclude_rules = LT01,RF01
```

It will run for all existing rules, excluding LT01 and RF01, for the dialect oracle


## Usage

You can create the docker by doing:

  ```bash
  docker build --no-cache -t codacy-sqlfluff:latest .
  ```

The docker is ran with the following command:

  ```bash
  docker run -it -v $srcDir:/src codacy-sqlfluff:latest
  ```

## Generate Docs

 1. Update the version in `requirements.txt`

 2. Run the DocGenerator to update all the patterns/descriptions and the patterns.xml (from all-patterns test)

    ```bash
    python<version> src/doc_generator.py
    ```

## Test

We use the [codacy-plugins-test](https://github.com/codacy/codacy-plugins-test) to test our external tools integration.
You can follow the instructions there to make sure your tool is working as expected.

## What is Codacy?

[Codacy](https://www.codacy.com/) is an Automated Code Review Tool that monitors your technical debt, helps you improve your code quality, teaches best practices to your developers, and helps you save time in Code Reviews.

### Among Codacy’s features:

 - Identify new Static Analysis issues
 - Commit and Pull Request Analysis with GitHub, BitBucket/Stash, GitLab (and also direct git repositories)
 - Auto-comments on Commits and Pull Requests
 - Integrations with Slack, HipChat, Jira, YouTrack
 - Track issues in Code Style, Security, Error Proneness, Performance, Unused Code and other categories

Codacy also helps keep track of Code Coverage, Code Duplication, and Code Complexity.

Codacy supports PHP, Python, Ruby, Java, JavaScript, and Scala, among others.

### Free for Open Source

Codacy is free for Open Source projects.