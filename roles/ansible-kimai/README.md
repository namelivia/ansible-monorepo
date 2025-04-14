# Kimai Ansible role [![Ansible Lint](https://github.com/namelivia/ansible-kimai/actions/workflows/ansible-lint.yml/badge.svg)](https://github.com/namelivia/ansible-kimai/actions/workflows/ansible-lint.yml)

The project depends on the collection `community.docker` but apparently this [cannot be listed as a dependency](https://github.com/ansible/ansible/issues/62847) so make sure you add it to your `requirements.yml` file like:

```yml
---

collections:
  - community.docker

roles:
  - src: https://github.com/namelivia/ansible-kimai
```

## Required variables
 - `alloy_host` Loki endpoint to send logs.
 - `domain_name` The domain name in which the app will be served from.
 - `host_port` Port to be mapped in the host machine.
 - `admin_mail` Email for the Kimai admin user.
 - `admin_pass` Password for the Kimai admin user.
 - `database_name` Name for the database Kimai will use.
 - `database_user` User that Kimai will use to connect to the database.
 - `database_password` Password for the user to connect to the database.
 - `mysql_root_password` Password for the MariaDB root user.
 - `dump_day` Day of the week in which the database will be backed up.
