#!/bin/bash
cd ../api/
pipenv requirements > requirements.txt
cd ../infra/
docker compose -f backend-dev.yml up --build