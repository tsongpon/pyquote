#!/bin/sh

current_dir=$(dirname "$BASH_SOURCE")

uwsgi --wsgi-file $current_dir/../pyquote/route/routing.py --py-autoreload 1 --callable app --http 127.0.0.1:5000
