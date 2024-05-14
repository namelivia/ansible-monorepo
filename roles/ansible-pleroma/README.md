# Pleroma Ansible role [![Ansible Lint](https://github.com/namelivia/ansible-pleroma/actions/workflows/ansible-lint.yml/badge.svg)](https://github.com/namelivia/ansible-pleroma/actions/workflows/ansible-lint.yml)

## This is a WIP

The project depends on the collection `community.docker` but apparently this [cannot be listed as a dependency](https://github.com/ansible/ansible/issues/62847) so make sure you add it to your `requirements.yml` file like:

```yml
---

collections:
  - community.docker

roles:
  - src: https://github.com/namelivia/ansible-pleroma
```

## Required variables (TODO: Update these)
 - `loki_url` Loki endpoint to send logs.
 - `domain_name` The domain name in which the app will be served from.
 - `host_port` Port to be mapped in the host machine.
