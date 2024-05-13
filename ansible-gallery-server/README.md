# Gallery client Ansible role [![Ansible Lint](https://github.com/namelivia/ansible-gallery-server/actions/workflows/ansible-lint.yml/badge.svg)](https://github.com/namelivia/ansible-gallery-server/actions/workflows/ansible-lint.yml)

## This is a WIP

The project depends on the collection `community.docker` but apparently this [cannot be listed as a dependency](https://github.com/ansible/ansible/issues/62847) so make sure you add it to your `requirements.yml` file like:

```yml
---

collections:
  - community.docker

roles:
  - src: https://github.com/namelivia/ansible-gallery-server
```

## Required variables

 - `loki_url` Loki endpoint to send logs.
 - `gallery_api_endpoint` API endpoint for connecting the client to the server API.
 - `user_info_service_endpoint` API endpoint for user information service.
 - `aws_access_key_id` Access key id to access the images S3 bucket.
 - `aws_secret_access_key` Secret key to access the images S3 bucket.
 - `aws_default_region` Region for the images S3 bucket.
 - `aws_bucket` Name for the images S3 bucket.
 - `domain_name` Domain name in wich the application will be served from.
 - `host_port` Port to be mapped in the host machine.
