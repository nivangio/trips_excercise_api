# Trips API 

This repository contains an API to serve amount of trips by week from the trips table. Given that it is an API, it is easily extensible to any other analytical purposes that may be needed from the Trips Table.

## About

The repository follows a standard Flask development and is ready to containerize using gunicorn

## Set-up

The solution is containerized and for that reason it can be ran using Docker. In order to keep database string connections as well as data source origins safe and flexible, they are passed as environment variables. To run the Docker, follow these steps:

  * Clone repository: `git clone https://github.com/nivangio/trips_excercise_api.git` (Avoid this step if you've done it before)
  * Go to the source folder: `cd trips_excercise_api`
  * Create a copy of .env.example file: `cp .env.example .env`
  * Edit .env file and pass corresponding values
  * Build docker image: `docker build . -t exercise_api` (**NOTE**: You may need sudo privileges)
  * Run docker image: `docker run --network host --name execution_api --env-file .env exercise_api` (**NOTE**: You may need sudo privileges)

## Usage

You can test the API on your local machine. The endpoint `/trips_by_week` contains two arguments:

  * date_from (mandatory): Can be a date in YYYY-MM-DD format specifying an absolute beginning or a rolling period based on actual time, such as `7days`
  * date_to (optional): Date in YYYY-MM-DD format. Ignored if date_from is in rolling period form
  * bbox: Represents a bounding box to search for orig_coords. 4 geometry points written as `lon1,lat1,lon2,lat2`
  * region: Name of the region. Ignored if bbox is passed

If none of `bbox` or `region` are passed, the application raises a bad request. Below some valid calls examples. The examples are written assuming you are serving the API with the Docker above

  * http://localhost:8000/trips_by_week?date_from=2017-01-01&region=Turin
  * http://localhost:8000/trips_by_week?date_from=2017-01-01&bbox=7,45,8,50
  * http://localhost:8000/trips_by_week?date_from=1500days&bbox=7,45,8,50

**Note**: The API supports, `minutes`, `hours`, `days` and `weeks` only
