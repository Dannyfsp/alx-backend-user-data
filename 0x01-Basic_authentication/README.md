# Basic Authentication

## Bachground Context
In this project, we learnt what the authentication process means and how to implement a **Basic Authentication** on a simple API.

In the industry, we should not implement our own Basic authentication system and use a module or framework(like in Python-Flask: [Flask-HTTPAuth](https://intranet.alxswe.com/rltoken/rpsPy0M3_FJuCLGNPUbmvg) instead. Here, for the learning purpose, we walked through each step of this mechanism to understand it by doing.

## Resources
**Read or watch:**
- [REST API Authentication Mechanisms](https://intranet.alxswe.com/rltoken/ssg5umgsMk5jKM8WRHk2Ug)
- [Base64 in Python](https://intranet.alxswe.com/rltoken/RpaPRyKx1rdHgRSUyuPfeg)
- [HTTP header Authorization](https://intranet.alxswe.com/rltoken/WlARq8tQPUGQq5VphLKM4w)
- [Flask](https://intranet.alxswe.com/rltoken/HG5WXgSja5kMa29fbMd9Aw)
- [Base64 - concept](https://intranet.alxswe.com/rltoken/br6Rp4iMaOce6EAC-JQnOw)

## Learning Objectives
At the end of this project, we are expected to be able to explain to anyone, **without the help of Google:**
- What authentication means
- What Base64 is
- How to encode a string in Base64
- What Basic authentication means
- How to send the Authorization header

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
