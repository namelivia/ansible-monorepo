# Ansible Tink Firefly Endpoint Ansible role [![Ansible Lint](https://github.com/namelivia/ansible-tink-firefly-endpoint/actions/workflows/ansible-lint.yml/badge.svg)](https://github.com/namelivia/ansible-tink-firefly-endpoint/actions/workflows/ansible-lint.yml)

## This is a WIP

The project depends on the collection `community.docker` but apparently this [cannot be listed as a dependency](https://github.com/ansible/ansible/issues/62847) so make sure you add it to your `requirements.yml` file like:

```yml
---

collections:
  - community.docker

roles:
  - src: https://github.com/namelivia/ansible-tink-firefly-endpoint
```

## Required variables (TODO: Update these)
 - `alloy_host` Loki endpoint to send logs.
 - `host_port` Port to be mapped in the host machine.
 - `tink_client_id` Your Tink Client Id.
 - `tink_client_secret` Your Tink Client Secret.
 - `tink_callback_uri`: Callback URI for tink.
 - `notifications_service_endpoint`: Endpoint for the notifications service.
