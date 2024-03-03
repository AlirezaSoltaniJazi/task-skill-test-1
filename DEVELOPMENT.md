# Python + Appium + Selenium + Android

## Install necessary packages

```shell
pipenv install pytest Appium-Python-Client pre-commit python-json-logger assertpy
```

## Install other tools

```shell
npm install -g appium
```

```shell
appium driver list --installed
```

```shell
appium driver install uiautomator2
```

```shell
appium --allow-insecure chromedriver_autodownload
```

```shell
appium driver install chromium
```

## Linter

- `pre-commit`: A multi-language package manager for pre-commit hooks that manages the installation and execution of any
  hook written in any language before every commit³.

### Install

```shell
pipenv install pre-commit
```

### Check Version

```shell
pre-commit --version
```

### Create Simple Config

```shell
pre-commit sample-config
```

#### Recommended Hooks

```text
https://github.com/pre-commit/pre-commit-hooks
https://github.com/Lucas-C/pre-commit-hooks-safety
https://github.com/PyCQA/bandit
pylint
https://github.com/psf/black
https://github.com/pre-commit/mirrors-mypy
```

### Create pylint Config (It's necessary for pre-commit config)

```shell
pylint --generate-rcfile >.pylintrc
```

### Run (Execution)

```shell
pre-commit run
```