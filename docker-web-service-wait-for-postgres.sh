#!/bin/sh

set -e

until PGPASSWORD=$POSTGRES_PASSWORD psql -h "$POSTGRES_HOST" -U "$POSTGRES_USER" -d "$POSTGRES_DB" -c '\q'; do
  >&2 echo "Postgres is NOT available yet - Sleeping..."
  sleep 2
done

>&2 echo "Postgres is up!"
