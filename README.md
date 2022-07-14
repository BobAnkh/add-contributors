# add-contributors

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/b8d0af034c5c4699805c6aca898787e7)](https://app.codacy.com/manual/bobankhshen/add-contributors?utm_source=github.com&utm_medium=referral&utm_content=BobAnkh/add-contributors&utm_campaign=Badge_Grade_Dashboard)
![GitHub release (latest by date)](https://img.shields.io/github/v/release/BobAnkh/add-contributors?color=orange&logo=github-actions)
![language-python](https://img.shields.io/github/languages/top/BobAnkh/add-contributors?logo=python&logoColor=yellow)
![LICENSE Apache-2.0](https://img.shields.io/github/license/BobAnkh/add-contributors?logo=apache)

A Github Action to add contributors to your markdown file(i.e. README.md) automatically on schedule or triggered by events

Specifically handle unreachable Chinese context (着重解决了中文内容乱码的问题)

Feel free to submit a pull request or an issue, but make sure to follow the templates

Welcome contributors to improve this project together!

## Usage

Create a workflow file such as `.github/workflows/contributors.yml` (you can find it in this repo)

```yaml
name: Add contributors
on:
  schedule:
    - cron:  '20 20 * * *'
# push:
#   branches:
#     - master

jobs:
  add-contributors:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v2
    - uses: BobAnkh/add-contributors@master
      with:
        CONTRIBUTOR: '### Contributors'
        COLUMN_PER_ROW: '6'
        ACCESS_TOKEN: ${{secrets.GITHUB_TOKEN}}
        IMG_WIDTH: '100'
        FONT_SIZE: '14'
        PATH: '/README.md'
        COMMIT_MESSAGE: 'docs(README): update contributors'
        AVATAR_SHAPE: 'round'
```

### Parameters

| Parameter            | Description                                                 | Required | Default                                            |
| -------------------- | ----------------------------------------------------------- | -------- | -------------------------------------------------- |
| REPO_NAME            | Repository name                                             | no       | `''` which means current repository                |
| CONTRIBUTOR          | Where you want to add contributors list                     | no       | `### Contributors`                                 |
| COLUMN_PER_ROW       | Number of contributors per row                              | no       | `6`                                                |
| ACCESS_TOKEN         | Github Access Token                                         | yes      | You can just pass `${{secrets.GITHUB_TOKEN}}`      |
| IMG_WIDTH            | Width of img                                                | no       | `100`                                              |
| FONT_SIZE            | Font size of name (px)                                      | no       | `14`                                               |
| PATH                 | Path to the file you want to add contributors' list         | no       | `/README.md`                                       |
| BRANCH               | The branch to update file specified in PATH                 | no       | `''` which means default branch                    |
| PULL_REQUEST         | Open a new pull request if set to a target branch name      | no       | `''` which means not open pull request by default  |
| COMMIT_MESSAGE       | commit message                                              | no       | `docs(README): update contributors`                |
| AVATAR_SHAPE         | Set `round` for round avatar and `square` for square avatar | no       | square                                             |
| IGNORED_CONTRIBUTORS | Ignored contributors, seperated by comma                    | no       | `''`                                               |

> NOTE: You should leave a blank line after the `CONTRIBUTOR` line for the first time
>
> NOTE: Github seems not support image style in markdown file rendering yet
>
> NOTE: `IGNORED_CONTRIBUTORS` takes **display name** not **username**
> 
> NOTE: `PULL_REQUEST` must be used with `BRANCH` together, both **should be provided** if you want to **open a pull request**

## Maintainer

[@BobAnkh](https://github.com/BobAnkh)

## How to contribute

You should follow our [Code of Conduct](/CODE_OF_CONDUCT.md).

See [CONTRIBUTING GUIDELINES](/CONTRIBUTING.md) for contributing conventions.

Make sure to pass all the tests before submitting your code. You can conduct `pytest -ra` at the root directory to run all tests.

You can use local mode when develope it on your local machine, here is the command-line help info:

```console
usage: main.py [-h] [-m MODE] [-f FILE] [-o OUTPUT] [-t TOKEN]

optional arguments:
  -h, --help            show this help message and exit
  -m MODE, --mode MODE  choose to use local-dev mode or on github action mode.
                        Valid values are 'local' or 'github'
  -f FILE, --file FILE  configuration file to read from when running local-dev
                        mode
  -o OUTPUT, --output OUTPUT
                        output file when running local-dev mode
  -t TOKEN, --token TOKEN
                        Github Access Token
```

### Contributors

<table>
<tr>
    <td align="center" style="word-wrap: break-word; width: 150.0; height: 150.0">
        <a href=https://github.com/BobAnkh>
            <img src=https://avatars.githubusercontent.com/u/44333669?v=4 width="100;"  style="border-radius:50%;align-items:center;justify-content:center;overflow:hidden;padding-top:10px" alt=Yixin Shen/>
            <br />
            <sub style="font-size:14px"><b>Yixin Shen</b></sub>
        </a>
    </td>
    <td align="center" style="word-wrap: break-word; width: 150.0; height: 150.0">
        <a href=https://github.com/baileythegreen>
            <img src=https://avatars.githubusercontent.com/u/12277715?v=4 width="100;"  style="border-radius:50%;align-items:center;justify-content:center;overflow:hidden;padding-top:10px" alt=Bailey Harrington/>
            <br />
            <sub style="font-size:14px"><b>Bailey Harrington</b></sub>
        </a>
    </td>
    <td align="center" style="word-wrap: break-word; width: 150.0; height: 150.0">
        <a href=https://github.com/casperklein>
            <img src=https://avatars.githubusercontent.com/u/590174?v=4 width="100;"  style="border-radius:50%;align-items:center;justify-content:center;overflow:hidden;padding-top:10px" alt=Casper/>
            <br />
            <sub style="font-size:14px"><b>Casper</b></sub>
        </a>
    </td>
</tr>
</table>

## LICENSE

[Apache-2.0](/LICENSE) © BobAnkh
