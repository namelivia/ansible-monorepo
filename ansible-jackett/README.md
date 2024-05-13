# Jackett Ansible role [![Ansible Lint](https://github.com/namelivia/ansible-jackett/actions/workflows/ansible-lint.yml/badge.svg)](https://github.com/namelivia/ansible-jackett/actions/workflows/ansible-lint.yml)

The project depends on the collection `community.docker` but apparently this [cannot be listed as a dependency](https://github.com/ansible/ansible/issues/62847) so make sure you add it to your `requirements.yml` file like:

```yml
---

collections:
  - community.docker

roles:
  - src: https://github.com/namelivia/ansible-jackett
```

## Required variables
 - `loki_url` Loki endpoint to send logs.
 - `backup_day` Day of the week in which the config will be backed up.
