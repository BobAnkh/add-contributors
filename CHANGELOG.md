# CHANGELOG

## Unreleased

Changes unreleased.

### Bug Fixes

- local:
  - add args-specify config file ([774a109](https://github.com/BobAnkh/add-contributors/commit/774a10968205067ec224f5fce2e4c28b9f83d1bb))

## [v0.2.0](https://github.com/BobAnkh/add-contributors/releases/tag/v0.2.0) - 2021-07-16 06:47:07

Add a new feature proposed in #46 to exclude certain contributors(e.g.  @renovate-bot and @codacy-badger)

Resolves: #46 

### Feature

- contributor:
  - support to ignore ocntributors ([d049565](https://github.com/BobAnkh/add-contributors/commit/d0495656fe47ec6cec1837b7bcf0a2b953ed9b92))

### Bug Fixes

- local:
  - resolve token read from file in local-dev mode ([5621757](https://github.com/BobAnkh/add-contributors/commit/5621757f674df38b746d57711f6d44a52442e23f))

### Documentation

- contributor:
  - update params usage ([2acb218](https://github.com/BobAnkh/add-contributors/commit/2acb2184554d1984a2e956f809b7490121cc980d))

- README:
  - update contributors ([969bc58](https://github.com/BobAnkh/add-contributors/commit/969bc58d3e0e3b6e71083ef0c6631ff1fa696750))
  - add info for tests ([6647d3d](https://github.com/BobAnkh/add-contributors/commit/6647d3d22547d2a5865e2b3d1bf24e92f076b5fa))

### Performance Improvements

- Dockerfile:
  - merge layers ([1f8ecc6](https://github.com/BobAnkh/add-contributors/commit/1f8ecc6677001e72a8498a37b2c4d04d59a5587b))

## [v0.1.0](https://github.com/BobAnkh/add-contributors/releases/tag/v0.1.0) - 2021-01-09 04:21:08

Refactor the data structure. No breaking changes. Prepare to add some tests

Add local mode for developing on local machine.

### Feature

- mode:
  - add local-dev mode ([c4e8115](https://github.com/BobAnkh/add-contributors/commit/c4e8115850f4148323689371463396d8dd6e272a)) ([#36](https://github.com/BobAnkh/add-contributors/pull/36))

### Documentation

- README:
  - update info for local mode ([3f02f72](https://github.com/BobAnkh/add-contributors/commit/3f02f720122e6f9015e5cdaeaea8beac18cef2e4))
  - fix a typo ([90eedc1](https://github.com/BobAnkh/add-contributors/commit/90eedc1d8dae57ef168856d08ccf9758b23bbef2))

### Refactor

- main:
  - uncouple data and api to github ([27b5e5b](https://github.com/BobAnkh/add-contributors/commit/27b5e5b55a0b8134a4ebc2073b3267f06154a08c))

### Performance Improvements

- main:
  - use yaml.safe_load and add docstring ([44553f6](https://github.com/BobAnkh/add-contributors/commit/44553f6d59769836061740bebdecd422493bbd5e))

- data:
  - imporve data structure ([7098489](https://github.com/BobAnkh/add-contributors/commit/7098489d03873c0235edf349b24679f33400cc03))

## [v0.0.8](https://github.com/BobAnkh/add-contributors/releases/tag/v0.0.8) - 2020-12-12 00:47:26

Change layout of contributors table to make it more beautiful.

### Feature

- table-style:
  - change layout of contributors table (#34) ([54e695f](https://github.com/BobAnkh/add-contributors/commit/54e695f9222907293a2d42c98937678763518ce4)) ([#34](https://github.com/BobAnkh/add-contributors/pull/34))

### Bug Fixes

- locate:
  - change locate feature ([ef71274](https://github.com/BobAnkh/add-contributors/commit/ef71274049fccc95376b272ca95cacb32eaed9b8))

- branch:
  - support other branches ([259b7be](https://github.com/BobAnkh/add-contributors/commit/259b7be4bac24805894e343bb58595a6d0bfba80)) ([#32](https://github.com/BobAnkh/add-contributors/pull/32))

### Documentation

- README:
  - update contributors ([f229687](https://github.com/BobAnkh/add-contributors/commit/f2296872426a5a36168cdf73691035a3da5df4f1))

- CONTRIBUTING:
  - update style guide ([10dd8c7](https://github.com/BobAnkh/add-contributors/commit/10dd8c7c6d6b2504da3b973487236659827a7968))

## [v0.0.7](https://github.com/BobAnkh/add-contributors/releases/tag/v0.0.7) - 2020-12-06 05:28:10

Support other branches.

You can use format like `<branch>:<file>` in input `PATH`, e.g. `dev:/README.md`, to specify the branch of your file.

## [v0.0.6](https://github.com/BobAnkh/add-contributors/releases/tag/v0.0.6) - 2020-10-20 05:35:37

Add more ErrorLog to output, making it more easier to debug

### Feature

- ErrorLog:
  - enhace error log readabiity ([38100e5](https://github.com/BobAnkh/add-contributors/commit/38100e55eac669aaba90eac26cd0ccf4ba061a94)) ([#11](https://github.com/BobAnkh/add-contributors/pull/11))

### Bug Fixes

- dockerfile:
  - use chmod to deal with  execution permission issue ([1082568](https://github.com/BobAnkh/add-contributors/commit/10825686580c7fc9c4ad5206546b29197dcb684a))

### Documentation

- README:
  - update contributors ([3b36628](https://github.com/BobAnkh/add-contributors/commit/3b36628ac13c7f3cdc6d0d521150f39d1e25ee11))
  - update contributors ([79f4e9e](https://github.com/BobAnkh/add-contributors/commit/79f4e9e5557d1a8bd636bf770b158eb02ac27319))
  - update contributors ([d14fb80](https://github.com/BobAnkh/add-contributors/commit/d14fb809966275e9fd7adbae0ee38deba4ca7013))
  - add a new badge ([b5a61b6](https://github.com/BobAnkh/add-contributors/commit/b5a61b6dff51007e9b30dde6ea9ad90f5a9eee59))
  - update table format ([82edd07](https://github.com/BobAnkh/add-contributors/commit/82edd072da7bf65810fdf7ef77f482106acc2bb8))

- CONTRIBUTING:
  - update format ([000568d](https://github.com/BobAnkh/add-contributors/commit/000568dc0ced4809688d82b64648347618f890a1))
  - refactor to have styleguide ([4a472af](https://github.com/BobAnkh/add-contributors/commit/4a472afecff5695701245579a17f60731fa8cccc))

- CONTRIBUTING.md:
  - change a word ([d285f3d](https://github.com/BobAnkh/add-contributors/commit/d285f3d387f52d051f6b3e9a3041a6310ab9b5d1))
  - fix a typo ([efe4f7a](https://github.com/BobAnkh/add-contributors/commit/efe4f7af7793b1031e58883e2f90331c6fada4da))

## [v0.0.5](https://github.com/BobAnkh/add-contributors/releases/tag/v0.0.5) - 2020-08-10 07:02:43

See [CHANGELOG](https://github.com/BobAnkh/add-contributors/blob/master/CHANGELOG.md) for changes

## [v0.0.4](https://github.com/BobAnkh/add-contributors/releases/tag/v0.0.4) - 2020-07-30 02:53:51

See [CHANGELOG](https://github.com/BobAnkh/add-contributors/blob/master/CHANGELOG.md) for changes

### Bug Fixes

- main:
  - deal with file not found error ([a0bf0ee](https://github.com/BobAnkh/add-contributors/commit/a0bf0ee6a8c6f0158cfc9c7a4219814c9e29fa29))

### Documentation

- README:
  - welcome contributors ([ddf2141](https://github.com/BobAnkh/add-contributors/commit/ddf21416a978acf30e75080630a33c678e8f5922))
  - add notes of avatar shape ([1636a56](https://github.com/BobAnkh/add-contributors/commit/1636a56530d8bbc3bbf78b220ae4e2344084297a))
  - update contributors ([ec79cb0](https://github.com/BobAnkh/add-contributors/commit/ec79cb0a7fa85d2a4c0825079242bc358dd12b85))

## [v0.0.3](https://github.com/BobAnkh/add-contributors/releases/tag/v0.0.3) - 2020-07-28 16:06:26

See [CHANGELOG](https://github.com/BobAnkh/add-contributors/blob/master/CHANGELOG.md) for changes

### Feature

- avatar:
  - add new attribute to choose shape ([1f87152](https://github.com/BobAnkh/add-contributors/commit/1f87152794ac246c9239846cbfb8133ba26c012b)) ([#3](https://github.com/BobAnkh/add-contributors/pull/3))
  - add option for avatar shape ([b366ced](https://github.com/BobAnkh/add-contributors/commit/b366cedfa81633570bc482b009723005500cfbaa)) ([#3](https://github.com/BobAnkh/add-contributors/pull/3))

### Documentation

- usage:
  - update parameters and example ([2a1515a](https://github.com/BobAnkh/add-contributors/commit/2a1515a6ead2f2cd0bb8318e98135d6c2e5faf0a)) ([#3](https://github.com/BobAnkh/add-contributors/pull/3))

- *:
  - add CONTRIBUTING.md ([bd43b70](https://github.com/BobAnkh/add-contributors/commit/bd43b70b6749d162ed0ccfec8b547eb1184600b2))

- README:
  - update introduction and contributing ([2eeb56c](https://github.com/BobAnkh/add-contributors/commit/2eeb56cf080102e25f3c9ee527901c3c49c0b098))

## [v0.0.2](https://github.com/BobAnkh/add-contributors/releases/tag/v0.0.2) - 2020-07-27 01:58:37

v0.0.2

### Feature

- entrypoint:
  - add main script to be excuted ([fdd630e](https://github.com/BobAnkh/add-contributors/commit/fdd630e85b7ebac74587c65e3be476ff963122f9))

- docker:
  - use entrypoint.sh ([ae5fa78](https://github.com/BobAnkh/add-contributors/commit/ae5fa78b6f261bc7e749b5aa6de39b1e6800cbc0))

### Bug Fixes

- main:
  - fix the format for first time ([4cb8252](https://github.com/BobAnkh/add-contributors/commit/4cb8252210addd677b7c6ca30a8b683b36a7b554))
  - fix the format for first time ([ad55b4b](https://github.com/BobAnkh/add-contributors/commit/ad55b4b73ce4e569f9499c98ece268d76327f3de))
  - fix a typo ([935c6c2](https://github.com/BobAnkh/add-contributors/commit/935c6c24f8cec43c2dd66764dd13e0b474c8add1))
  - correct permission to be excuted ([069bee7](https://github.com/BobAnkh/add-contributors/commit/069bee752cb61ef83958b5ffa628e8137324915a))

- entrypoint:
  - correct permission to be excuted ([72cf66c](https://github.com/BobAnkh/add-contributors/commit/72cf66c534174f6f9dd5a268f19044c8274e0c6d))

- action:
  - fix secrets typo ([ccc0500](https://github.com/BobAnkh/add-contributors/commit/ccc05002f06f01a61e2a78df7d33b74864ed50f0))

- token:
  - change token-required to be true ([e91599c](https://github.com/BobAnkh/add-contributors/commit/e91599cc099f4da32fbd95fd5ce58249502e69fe))

### Documentation

- README:
  - add more info in usage ([677c599](https://github.com/BobAnkh/add-contributors/commit/677c5994f8970e16d9eee54d305b231b409a61e8))
  - update contributors ([f228298](https://github.com/BobAnkh/add-contributors/commit/f228298b8f6ccc75e93cc66cc27df7ac05544a0d))
  - update contributors ([250250e](https://github.com/BobAnkh/add-contributors/commit/250250e71e78ede89231e4f0fe4a05ca7ceb9b21))
  - update contributors ([dc7f3f2](https://github.com/BobAnkh/add-contributors/commit/dc7f3f2b9c0ca2baeebb100b6333c04960f08ce2))

## [v0.0.1](https://github.com/BobAnkh/add-contributors/releases/tag/v0.0.1) - 2020-07-26 15:54:01

Initial release

### Documentation

- README:
  - add README ([f5b764f](https://github.com/BobAnkh/add-contributors/commit/f5b764f54540cc526b924bc0852582cff3a85510))

\* *This CHANGELOG was automatically generated by [auto-generate-changelog](https://github.com/BobAnkh/auto-generate-changelog)*
