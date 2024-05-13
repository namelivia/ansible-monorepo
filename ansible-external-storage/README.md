# External storage Ansible role [![Ansible Lint](https://github.com/namelivia/ansible-external-storage/actions/workflows/ansible-lint.yml/badge.svg)](https://github.com/namelivia/ansible-external-storage/actions/workflows/ansible-lint.yml)

The project depends on the collection `ansible.posix` but apparently this [cannot be listed as a dependency](https://github.com/ansible/ansible/issues/62847) so make sure you add it to your `requirements.yml` file like:

```yml
---

collections:
  - ansible.posix

roles:
  - src: https://github.com/namelivia/ansible-external-storage
```

## Required variables
 - `external_storage_device_id` UUID for the device to be mounted
 - `target_directory` Target directory in which the device will be mounted
