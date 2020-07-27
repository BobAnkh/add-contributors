# add-contributors

A Github Action to add contributors to your markdown file(i.e. README.md) automatically on schedule

Specifically handle unreachable Chinese context

着重解决了中文内容乱码的问题

Now is under test

## Usage

Create a workflow file such as `.github/workflows/contributors.yml`

```yaml
name: Add contributors
on:
  schedule:
    - cron:  '20 20 * * *'

jobs:
  add-contributors:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v2
    - uses: BobAnkh/add-contributors@master
      with:
        REPO_NAME: 'BobAnkh/add-contributors'
        CONTRIBUTOR: '### Contributors'
        COLUMN_PER_ROW: '6'
        ACCESS_TOKEN: ${{secrets.GITHUB_TOKEN}}
        IMG_WIDTH: '100'
        FONT_SIZE: '14'
        PATH: '/README.md'
        COMMIT_MESSAGE: 'docs(README): update contributors'
```

### Parameters

| Parameter | Description | Required | Default |
| --- | --- | --- | --- |
| REPO_NAME| Repository name | yes | - |
| CONTRIBUTOR | Where you want to add contributors list | no | `### Contributors`|
| COLUMN_PER_ROW | Number of contributors per row | no | `6` |
| ACCESS_TOKEN | Github Access Token | yes | You can just pass `${{secrets.GITHUB_TOKEN}}` |
| IMG_WIDTH | Width of img | no | `100` |
| FONT_SIZE | Font size of name (px) | no | `14` |
| PATH | Path to the file you want to add contributors' list | no | `/README.md` |
| COMMIT_MESSAGE | commit message | no | `docs(README): update contributors` |

> NOTE: You should leave a blank line after the `CONTRIBUTOR` line for the first time

## Maintainer

[@BobAnkh](https://github.com/BobAnkh)

## How to contribute

See [CONTRIBUTING GUIDELINES](/CONTRIBUTING.md) for details

### Contributors

<table>
<tr>
    <td align="center">
        <a href=https://github.com/BobAnkh>
            <img src=https://avatars2.githubusercontent.com/u/44333669?v=4 width="100;" alt=BobAnkh/>
            <br />
            <sub style="font-size:14px"><b>BobAnkh</b></sub>
        </a>
    </td>
</tr>
</table>## LICENSE

[Apache-2.0](/LICENSE) © BobAnkh
