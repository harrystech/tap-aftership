# tap-aftership

`tap-aftership` is a Singer tap for AfterShip. Fetches trackings from the AfterShip API
using the [trackings API endpoint](https://www.aftership.com/docs/aftership/ce171c8e31139-get-trackings)

Built with the [Meltano Tap SDK](https://sdk.meltano.com) for Singer Taps.

## Installation

Install from PyPi:

```bash
pipx install tap-aftership
```

Install from GitHub:

```bash
pipx install git+https://github.com/ORG_NAME/tap-aftership.git@main
```

## Capabilities

* `catalog`
* `state`
* `discover`
* `about`
* `stream-maps`
* `schema-flattening`

## Settings

| Setting             | Required | Default | Description                                                                                                                                 |
|:--------------------|:--------:|:-------:|:--------------------------------------------------------------------------------------------------------------------------------------------|
| api_key             | True     | None    | The token to authenticate against the API service                                                                                           |
| start_date          | False    | None    | The earliest record date to sync (by time of update)                                                                                        |
| end_date            | False    | None    | The latest record date to sync (by time of update)                                                                                          |
| stream_maps         | False    | None    | Config object for stream maps capability. For more information check out [Stream Maps](https://sdk.meltano.com/en/latest/stream_maps.html). |
| stream_map_config   | False    | None    | User-defined config values to be used within map expressions.                                                                               |
| flattening_enabled  | False    | None    | 'True' to enable schema flattening and automatically expand nested properties.                                                              |
| flattening_max_depth| False    | None    | The max depth to flatten schemas.                                                                                                           |

A full list of supported settings and capabilities is available by running: `tap-aftership --about`

### Configure using environment variables

This Singer tap will automatically import any environment variables within the working directory's
`.env` if the `--config=ENV` is provided, such that config values will be considered if a matching
environment variable is set either in the terminal context or in the `.env` file.

### Source Authentication and Authorization

An API key can be created in the AfterShip UI following [these
instructions](https://www.aftership.com/docs/aftership/quickstart/api-quick-start#:~:text=Get%20the%20API%20key,to%20generate%20your%20API%20key.).
Note that this tap currently only supports the [legacy API
key](https://www.aftership.com/docs/aftership/quickstart/authentication#4-legacy-api-keys)
format.

## Usage

You can easily run `tap-aftership` by itself or in a pipeline using [Meltano](https://meltano.com/).

### Executing the Tap Directly

```bash
tap-aftership --version
tap-aftership --help
tap-aftership --config CONFIG --discover > ./catalog.json
```

## Developer Resources

Follow these instructions to contribute to this project.

### Initialize your Development Environment

```bash
pipx install poetry
poetry install
```

### Create and Run Tests

Create tests within the `tap_aftership/tests` subfolder and
  then run:

```bash
poetry run pytest
```

You can also test the `tap-aftership` CLI interface directly using `poetry run`:

```bash
poetry run tap-aftership --help
```

### Testing with [Meltano](https://www.meltano.com)

_**Note:** This tap will work in any Singer environment and does not require Meltano.
Examples here are for convenience and to streamline end-to-end orchestration scenarios._

Next, install Meltano (if you haven't already) and any needed plugins:

```bash
# Install meltano
pipx install meltano
# Initialize meltano within this directory
cd tap-aftership
meltano install
```

Now you can test and orchestrate using Meltano:

```bash
# Test invocation:
meltano invoke tap-aftership --version
# OR run a test `elt` pipeline:
meltano elt tap-aftership target-jsonl
```

### SDK Dev Guide

See the [dev guide](https://sdk.meltano.com/en/latest/dev_guide.html) for more instructions on how to use the SDK to
develop your own taps and targets.
