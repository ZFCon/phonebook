##### *Start the Project*

##### *Execute make migrate, so that the table gets created in the database*
`docker-compose run web python manage.py migrate`


##### *Create super user for django admin*
`docker-compose run web python manage.py createsuperuser`

 
##### *To access the database (get the container id using cmd - docker ps)*
`docker exec -it 728f78dc6a12 bash`

`psql -U postgres`

##### *build the docker compose file*
`docker-compose up --build`


##### *To start the project*
`docker-compose up`