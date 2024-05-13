# Recipe Suggestions Ansible role [![Ansible Lint](https://github.com/namelivia/recipe-suggestions/actions/workflows/ansible-lint.yml/badge.svg)](https://github.com/namelivia/recipe-suggestions/actions/workflows/ansible-lint.yml)

The project depends on the collection `community.docker` but apparently this [cannot be listed as a dependency](https://github.com/ansible/ansible/issues/62847) so make sure you add it to your `requirements.yml` file like:

```yml
---

collections:
  - community.docker

roles:
  - src: https://github.com/namelivia/ansible-recipe-suggestions
```

## Required variables

 - `loki_url` Loki endpoint to send logs.
 - `notifications_service_endpoint`: Notifications Service Endpoint.
