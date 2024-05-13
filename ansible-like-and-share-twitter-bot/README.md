# Like And Share Twitter Bot Ansible role [![Ansible Lint](https://github.com/namelivia/ansible-like-and-share-twitter-bot/actions/workflows/ansible-lint.yml/badge.svg)](https://github.com/namelivia/ansible-like-and-share-twitter-bot/actions/workflows/ansible-lint.yml)

The project depends on the collection `community.docker` but apparently this [cannot be listed as a dependency](https://github.com/ansible/ansible/issues/62847) so make sure you add it to your `requirements.yml` file like:

```yml
---

collections:
  - community.docker

roles:
  - src: https://github.com/namelivia/ansible-like-and-share-twitter-bot
```

## Required variables

 - `loki_url` Loki endpoint to send logs.
 - `consumer_key`: Your Twitter account consumer key.
 - `consumer_secret`: Your Twitter account consumer secret.
 - `access_token_key`: Your Twitter account access token key.
 - `access_token_secret`: Your Twitter account access token secret.
 - `search_string`: The [Twitter search](https://help.twitter.com/en/using-twitter/twitter-advanced-search) string. e.g. `cats OR kitties`
 - `chance_to_act`: The chances to actually do something or just idle (from 0 to 100). e.g. `40`
 - `chance_to_favorite`: The chances to mark a tweet as favorite (from 0 to 100). e.g. `20`
 - `chance_to_follow`: The chances to follow the profile who tweeted (from 0 to 100). e.g. `15`
 - `language`: The language code for the [Twitter search](https://help.twitter.com/en/using-twitter/twitter-advanced-search). e.g. `en`
 - `idle_period`: The number of seconds the script will wait before executing. e.g. `900`
 - `sentry_url`: If set errors will be sent to [Sentry](https://sentry.io)
