# Postgres Ansible role [![Ansible Lint](https://github.com/namelivia/ansible-postgres/actions/workflows/ansible-lint.yml/badge.svg)](https://github.com/namelivia/ansible-postgres/actions/workflows/ansible-lint.yml)

## This is a WIP

The project depends on the collection `community.docker` but apparently this [cannot be listed as a dependency](https://github.com/ansible/ansible/issues/62847) so make sure you add it to your `requirements.yml` file like:

```yml
---

collections:
  - community.docker

roles:
  - src: https://github.com/namelivia/ansible-postgres
```

## Required variables
 - `alloy_host` Loki endpoint to send logs.
 - `postgres_username` Username for Postgres.
 - `postgres_password` Password for Postgres.
