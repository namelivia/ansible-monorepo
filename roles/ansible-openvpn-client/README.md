# OpenVPN client Ansible role [![Ansible Lint](https://github.com/namelivia/ansible-openvpn-client/actions/workflows/ansible-lint.yml/badge.svg)](https://github.com/namelivia/ansible-openvpn-client/actions/workflows/ansible-lint.yml)

## This is a WIP

The project depends on the collection `community.docker` but apparently this [cannot be listed as a dependency](https://github.com/ansible/ansible/issues/62847) so make sure you add it to your `requirements.yml` file like:

```yml
---

collections:
  - community.docker

roles:
  - src: https://github.com/namelivia/ansible-openvpn-client
```

## Required variables (TODO: Update these)
 - `cloudwatch_region` Cloudwatch region to send the logs to.
 - `cloudwatch_log_group` Cloudwatch log group to send the logs to.
 - `domain_name` The domain name in which the app will be served from.
