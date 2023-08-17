#!/bin/bash

# Start Django development server
python manage.py runserver 0.0.0.0:8000 &

# Wait for the database to be ready
sleep 10

# Apply migrations
python manage.py migrate

# Keep the script running
tail -f /dev/null
