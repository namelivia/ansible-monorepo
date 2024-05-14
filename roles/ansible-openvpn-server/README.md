# OpenVPN sever Ansible role [![Ansible Lint](https://github.com/namelivia/ansible-openvpn-server/actions/workflows/ansible-lint.yml/badge.svg)](https://github.com/namelivia/ansible-openvpn-server/actions/workflows/ansible-lint.yml)

## About

This is an Ansible role to install and configure [OpenVPN](https://openvpn.net/) inside a Docker container.
Logs are sent to [Cloudwatch](https://aws.amazon.com/cloudwatch/).

Currently the configuration (the whole contents for `/etc/openvpn`) are meant to be copied over, that's why this path is needed.

It is also meant to be run along with [jwilder/nginx-proxy](https://hub.docker.com/r/jwilder/nginx-proxy), that's also why it needs a `doman_name` variable.

## Disclaimer

The project depends on the collection `community.docker` but apparently this [cannot be listed as a dependency](https://github.com/ansible/ansible/issues/62847) so make sure you add it to your `requirements.yml` file like:

```yml
---

collections:
  - community.docker

roles:
  - src: https://github.com/namelivia/ansible-openvpn-server
```

## Required variables

 - `cloudwatch_region` Cloudwatch region to send the logs to.
 - `cloudwatch_log_group` Cloudwatch log group to send the logs to.
 - `openvpn_config_folder` The path in which the openvpn configuration will be copied from.
 - `domain_name` The domain name in which the app will be served from.
