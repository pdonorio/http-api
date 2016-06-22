
# REST API development base

This is an attempt to have a multi-container micro-services environment
to easily develop REST API in Python.

--

## Pre-requisites

Before starting please make sure that you have installed on your system:

* [Docker](http://docs.docker.com/) 1.11+
* [docker-compose](https://docs.docker.com/compose/) 1.7+

## Quick start

If you need to jump in as soon as possible:

```bash
# Clone this repository
git clone https://github.com/pdonorio/restapi-template.git
# Init services
./do init
# Then run the final services
./do DEVELOPMENT
### Develop from here!

# You may also create another shell to mimic the API client
./do client_shell
/ # http GET http://apiserver/api/status

```

## Training

With the following commands you can setup your machine
to start training on handling data
from/to:
* iRODS (B2SAFE)
* and GraphDB (neo4j)

```bash
git clone https://github.com/pdonorio/restapi-template.git
./do init
./do training
```
