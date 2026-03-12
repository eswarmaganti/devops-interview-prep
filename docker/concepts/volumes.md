# Docker Volumes
Docker volumes are the preferred mechanism for persisting data generated and used by Docker containers, ensuring data is not lost when containers are stopped, removed, or rebuilt.

## Key Concepts
- **Persistence**: By Default, data written inside a container's writable layer is lost when the container is removed. Volumes store data outside the container's lifecycle on the host machine's filesystem, making it durable.
- **Management**: Volumes are managed entirely by Docker, unlike bind mounts which can reside anywhere on the host filesystem and be modified by non-Docker processes. Docker manages their creation, storage location and removal.
- **Sharing**: A single volume can be safely shared and mounted into multiple containers simultaneously, which is useful for shared databases, logging or data pipelines.
- **Performance**: Volumes offer better I/O performance compared to writing data into a container's writable layer, which involves a performance-reducing storage driver and union filesystem abstraction.
- **Portability**: Volumes work on both Linux and Windows containers, and can integrate with cloud providers and external storage systems using volume drivers, making then more portable than host-dependent bind mounts.

## Types of Volumes
- **Named Volume**: Created with a specific, user-defined name. They are easy to reference and reuse across different containers and are generally recommended for production environments
- **Anonymous Volumes**: Automatically assigned a random, unique name by Docker. They are useful for temporary storage when manual management isn't necessary.
- **Bind Mounts**: While not strictly volumes managed by the Docker daemon, they are a related storage mechanism that links a specific directory or file from the *host* system directly into the container. They are great for development workflows where you need immediate reflection of code changes between the host and container.
- **tmpfs Mounts**: Store data in the host machine's memory (RAM) and are purely ephemeral; data is lost when the container stops or the host reboots. They are suitable for sensitive data or temporary, high-speed caching.

```bash
# creating a container with volume mount
$ docker run -d --name flask-app -v myvol:/app -p 8000:8000 flask-app:1 
be6c32b3488c6a58a9ca52223ca832b5029c3f1c407aee08ba38c7bb906cf60f

# Listing running containers
$ docker container ps
CONTAINER ID   IMAGE                  COMMAND                  CREATED         STATUS         PORTS                                         NAMES
be6c32b3488c   flask-app:1            "gunicorn --bind 0.0…"   4 seconds ago   Up 3 seconds   0.0.0.0:8000->8000/tcp, [::]:8000->8000/tcp   flask-app

# listing the volumes 
$ docker volume ls
DRIVER    VOLUME NAME
local     myvol

# stopping and deleting the container
$ docker container stop be6c32b3488c
be6c32b3488c

$ docker container rm be6c32b3488c
be6c32b3488c

# listing the volume post container deletion
$ docker volume ls
DRIVER    VOLUME NAME
local     myvol

# Deleting the volume
$ docker volume rm myvol
myvol
```

Bind Mount Example
```bash
$ docker run -d --name flask-app --mount type=bind,src=$(pwd),target=/app --publish 8000:8000  flask-app:1
19f0184b091600a9088ac03cda8f4452e2f5f9b3fb964cce3e43b514d44bdc74
```