# FastAPI + Uvicorn + Nginx example

## Introduction

The idea behind this repo is to provide a sample or template to create FastAPI and Uvicorn service running through an Nginx reverse proxy.

## Repository structure

```
api-auth/
├─ ops/
│  ├─ *.sh (to be run locally and perform local tests)
├─ src/
│  ├─ *.py
├─ tests/
│  ├─ *.py (to be run locally or trigger by git/jenkins/drone or another CI/CD tool)
├─ README.md
```

### ops
Contains devops/operation files

### local_test
A directory containing scripts and configurations to trigger training and inference jobs locally.

* __serve-local.sh__: trigger the local serving container and launch a local flask API.
* __test-dir__: The directory that is mounted on the container with test data mounted everywhere that matches the schema of the container.
* __build_and_push.sh__: A script to trigger the container build and then push it to the AWS SageMaker.

### src
Module containing classes and helper functions.
We use the following libraries to create a production ready inference server container:

1. __nginx__ : https://www.nginx.com/
2. __gunicorn__ : https://gunicorn.org/ 
3. __gunicorn__ : https://uvicorn.org/ 
4. __FastAPI__ : https://fastapi.tiangolo.com/

We configure this container to trigger __serve__ script on start. The scripts on source folders are the following:

* __api.py__: The API interface with methods. 
* __serve__: the wrapper that starts the inference server. In most cases, you can use this file as is.
* __wsgi.py__: The startup shell for individual server workers. This only needs to be changed if you changed where predictor.py is located or if it was renamed.
* __nginx.conf__: The configuration of the nginx server.

### tests
Contains test files for model functions or code and specific business rule cases. You can run local tests with `pytest -v`.
