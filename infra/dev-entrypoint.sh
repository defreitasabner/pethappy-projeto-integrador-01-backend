#!/bin/bash
sleep 20
python manage.py migrate
python manage.py runserver 0.0.0.0:8000