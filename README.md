# aws-drf-playground 🚀

AWS Playground with Django DRF App

[![CI](https://github.com/Kosaaaaa/aws-drf-playground/actions/workflows/ci.yml/badge.svg)](https://github.com/Kosaaaaa/aws-drf-playground/actions/workflows/ci.yml)

## Description

Simple Django Rest Framework API with jokes. This is proof of concept of deploying dockerized apps onto AWS EC2
instance.

## Usage

1. Copy example env file and update it with your data
   `cp example.env .env`
2. Run Dev environment `docker-compose up`
3. Run Deployment-Ready environment `docker-compose -f docker-compose-deploy.yml up`
4. Try jokes endpoint `/api/core/jokes`
5. See docs at **DEV** `api/docs`

## Technologies

* ✅ CI - using github actions; runs on push to `master` branch and PRs
    * pre-commit checks
    * running django tests
* ✅ Dockerized app
    * project splitted into services
    * used healthcheck for postgres DB - django app should wait until it is ready to use
* ✅ OpenAPI 3.0 schema and docs using `drf-spectacular`
* ✅ JWT Authentication

## Changelog

* 1.0.0 - initial
* 1.1.0 - add JWT authentication
* 1.1.1 - add README badges
