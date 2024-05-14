# Nextcloud Ansible role [![Ansible Lint](https://github.com/namelivia/ansible-nextcloud/actions/workflows/ansible-lint.yml/badge.svg)](https://github.com/namelivia/ansible-nextcloud/actions/workflows/ansible-lint.yml)

The project depends on the collection `community.docker` but apparently this [cannot be listed as a dependency](https://github.com/ansible/ansible/issues/62847) so make sure you add it to your `requirements.yml` file like:

```yml
---

collections:
  - community.docker

roles:
  - src: https://github.com/namelivia/ansible-nextcloud
```

## Required variables
 - `loki_url` Loki endpoint to send logs.
 - `database_name` Name for the database Nextcloud will use.
 - `database_user` User that Nextcloud will use to connect to the database.
 - `database_password` Password for the user to connect to the database.
 - `mysql_root_password` Password for the MariaDB root user.
 - `dump_day` Day of the week in which the database will be backed up.
 - `backup_day` Day of the week in which the filesystem will be backed up.
 - `trusted_domains` Domains for the app to be executed from.
 - `admin_user` Nextcloud admin username
 - `admin_password` Nextcloud admin password
 - `host_port` Port to be mapped in the host machine.
