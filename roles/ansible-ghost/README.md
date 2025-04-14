# Ghost Ansible role [![Ansible Lint](https://github.com/namelivia/ansible-ghost/actions/workflows/ansible-lint.yml/badge.svg)](https://github.com/namelivia/ansible-ghost/actions/workflows/ansible-lint.yml)

The project depends on the collection `community.docker` but apparently this [cannot be listed as a dependency](https://github.com/ansible/ansible/issues/62847) so make sure you add it to your `requirements.yml` file like:

```yml
---

collections:
  - community.docker

roles:
  - src: https://github.com/namelivia/ansible-ghost
```

 - `database_name` Name for the database that will hold the data.
 - `database_user` Username for the user that will own the data on the database.
 - `database_password` Password for the user that will own the data on the database.
 - `dump_day` Day of the week in which the database will be dumped.
 - `backup_day` Day of the week in which the filesystem will be backed up.
 - `mysql_root_password` Password for admin user for the mariadb database.
 - `alloy_host` Loki endpoint to send logs.
 - `domain_name` The domain name in which the app will be served from.
