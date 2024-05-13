# Backups Ansible role [![Ansible Lint](https://github.com/namelivia/ansible-backups/actions/workflows/ansible-lint.yml/badge.svg)](https://github.com/namelivia/ansible-backups/actions/workflows/ansible-lint.yml)

This is the Ansible role I use to periodically backup all the content of what's in my servers in S3.

## Included tasks
 - `setup-s3-backups` Setup a recurrent task to save backups on s3.
 - `setup-file-backups` Setup a recurrent task to create important files backup.
 - `setup-mariadb-database-backups` Setup a recurrent task to backup a mariadb database.
 - `setup-postgres-database-backups` Setup a recurrent task to backup a postgres database.

## Required variables (TODO: Update this)

 - `application_name` Application name to create backups for.
 - `backups_bucket_name` Name of the S3 bucket that will hold the backups.
 - `gpg_recipient` Sets the recipient for GPG when encrypting the backups.
 - `dump_day` This is an optional variable, a rudimentary way to avoid all containers doing the backup at the same time and overloading the host.
