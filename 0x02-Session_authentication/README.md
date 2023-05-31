# Session Authentication

## Bachground Context
In this project, we will implement a **Session Authentication.**

In the industry, we should not implement our own Session authentication system and use a module or framework(like in Python-Flask: [Flask-HTTPAuth](https://intranet.alxswe.com/rltoken/rpsPy0M3_FJuCLGNPUbmvg) instead. Here, for the learning purpose, we walked through each step of this mechanism to understand it by doing.

## Resources
**Read or watch:**
- [REST API Authentication Mechanisms - Only the session auth part](https://intranet.alxswe.com/rltoken/oofk0VhuS0ZFZTNTVrQeaQ)
- [HTTP Cookie](https://intranet.alxswe.com/rltoken/peLV8xuJ4PDJMOVFqk-d2g)
- [Flask](https://intranet.alxswe.com/rltoken/HG5WXgSja5kMa29fbMd9Aw)
- [Flask Cookie](https://intranet.alxswe.com/rltoken/QYfI5oW6OHUmHDzwKV1Qsw)

## Learning Objectives
At the end of this project, we are expected to be able to explain to anyone, **without the help of Google:**
- What authentication means
- What session authentication means
- How Cookies are
- How to send Cookies
- How to parse Cookies

# Simple API

Simple HTTP API for playing with `User` model.


## Files

### `models/`

- `base.py`: base of all models of the API - handle serialization to file
- `user.py`: user model

### `api/v1`

- `app.py`: entry point of the API
- `views/index.py`: basic endpoints of the API: `/status` and `/stats`
- `views/users.py`: all users endpoints


## Setup

```
$ pip3 install -r requirements.txt
```


## Run

```
$ API_HOST=0.0.0.0 API_PORT=5000 python3 -m api.v1.app
```


## Routes

- `GET /api/v1/status`: returns the status of the API
- `GET /api/v1/stats`: returns some stats of the API
- `GET /api/v1/users`: returns the list of users
- `GET /api/v1/users/:id`: returns an user based on the ID
- `DELETE /api/v1/users/:id`: deletes an user based on the ID
- `POST /api/v1/users`: creates a new user (JSON parameters: `email`, `password`, `last_name` (optional) and `first_name` (optional))
- `PUT /api/v1/users/:id`: updates an user based on the ID (JSON parameters: `last_name` and `first_name`)
