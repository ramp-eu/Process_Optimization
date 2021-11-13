# Process Optimization

[![License: MIT](https://img.shields.io/github/license/ramp-eu/TTE.project1.svg)](https://opensource.org/licenses/MIT)
[![Docker badge](https://img.shields.io/docker/pulls/ramp-eu/TTE.project1.svg)](https://hub.docker.com/r/<org>/<repo>/)
<br/>
[![Documentation Status](https://github.com/ramp-eu/Process_Optimization)](https://github.com/ramp-eu/Process_Optimization
[![CI](https://github.com/ramp-eu/TTE.project1/workflows/CI/badge.svg)](https://github.com/ramp-eu/TTE.project1/actions?query=workflow%3ACI)
[![Coverage Status](https://coveralls.io/repos/github/ramp-eu/TTE.project1/badge.svg?branch=master)](https://coveralls.io/github/ramp-eu/TTE.project1?branch=master)
[![Codacy grade](https://img.shields.io/codacy/grade/99310c5c4332439197633912a99d2e3c)](https://app.codacy.com/manual/jason-fox/TTE.project1)
[![CII Best Practices](https://bestpractices.coreinfrastructure.org/projects/4187/badge)](https://bestpractices.coreinfrastructure.org/projects/4187)

Process Optimisation performs process quality and efficiency optimisation using nonlinear model predictive control. The
system learns the dynamics of the production process, an then it can predict the process output quality metrics given
the current values for the control parameters. The user can also make simulated predictions about the key quality
indicators with alternative control parameter values, so as to seek for better control. The system can also find optimal
control values given the desired output quality and optimisation constraints, and can thus be used as an advisory tool
for the operator or as an autonomous closed-loop controller.

## Contents

-   [Background](#background)
-   [Usage](#usage)
-   [API](#api)
-   [Testing](#testing)
-   [License](#license)

## Background

## Usage

1. `docker pull`
2. `docker run -p 6543:6543 process_optimization`
3. The API service will be then accessible via `http://localhost:6543/api/v1.0/`

## API

```text
Definition of the API interface:

Information about the API can be found in the [API documentation](http://localhost:6543/api/v1.0/) of the running docker container.

```

## License

[MIT](LICENSE) © <TTE>
