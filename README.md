# refresh-action

Updates a tool's [awesome-alternatives](https://awesome-alternatives.com) listing as soon as it
publishes a release, instead of waiting for the nightly refresh.

```yaml
on:
  release:
    types: [published]

permissions:
  id-token: write

jobs:
  awesome-alternatives:
    runs-on: ubuntu-latest
    steps:
      - uses: awesome-alternatives/refresh-action@v1
```

No token or secret to store. The action asks GitHub for an OIDC token with the audience
`awesome-alternatives` and sends it to the API. GitHub signs the `repository` claim in that token,
so a workflow can only ask for its own repository to be refreshed. Every tool listed from that
repository is refreshed, which covers monorepos with several entries.

The API refreshes a repository at most once every 10 minutes. A second call in that window is
answered, not queued.

The step never fails your workflow: an unlisted repository, a missing `id-token: write` or an API
that does not answer end in a warning, and the listing catches up at the next nightly refresh.

## Inputs

| Input | Default |
|---|---|
| `api-url` | `https://awesome-alternatives.com/api` |
| `audience` | `awesome-alternatives` |

## Without a workflow

Installing the [awesome-alternatives GitHub App](https://github.com/apps/awesome-alternatives) on
the repository does the same thing on every published release, with read-only access to its
contents. Either one is enough, and having both is harmless.

## License

MIT
