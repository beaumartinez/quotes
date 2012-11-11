#! /usr/bin/env bash

if [[ -n "$1" ]]; then
    HOST_ARGUMENT="-b $1"
fi

gunicorn quotes.wsgi $HOST_ARGUMENT
