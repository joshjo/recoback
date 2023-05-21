# Django Backend for Location Tracking

This is the backend API for a api tracking application that allows users to view the location of other devices in real-time and receive notifications when a truck passes near their registered location or follows a specific path. The backend is built with Django and supports web sockets with Django Channels for real-time functionality.

## Prerequisites

- Docker
- Docker Compose

## Installation

1. Clone the repository:

```
git clone https://github.com/[your-username]/backend.git
```

2. Change into the project directory:

```
cd backend
```

3. Build the Docker images:

```
docker-compose build
```

4. Set up the database:

```
docker-compose run web python manage.py migrate
```

5. Create a superuser:

```
docker-compose run web python manage.py createsuperuser
```

6. Start the development server:

```
docker-compose up
```

7. Exec the bin file

```
docker-compose exec web bash && launch_reco
```

The development server will be available at http://localhost:8000.

## Deployment

To deploy the app in production, you will need to build and run the Docker images on a production-grade web server. You will also need to set up a secure connection using SSL/TLS, as well as a reverse proxy server such as Nginx to handle incoming HTTP requests.

## Built With

- [Django](https://www.djangoproject.com/) - The web framework used
- [Django Channels](https://channels.readthedocs.io/en/latest/) - Used for real-time functionality via web sockets
- [PostgreSQL](https://www.postgresql.org/) - The database used (with the [PostGIS](https://postgis.net/) extension)
- [Docker](https://www.docker.com/) - Used for containerization
- [Docker Compose](https://docs.docker.com/compose/) - Used for defining and running multi-container Docker applications

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests.
