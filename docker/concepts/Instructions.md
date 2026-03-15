
## FROM
The `FROM` instruction is always the starting point in a Dockerfile and must be the first non-comment line. It defines the base image for your docker image.

```docker
FROM <image>
FROM <image>:<tag>
FROM <image>@<digest>
```

## MAINTAINER
The `MAINTAINER` instruction is used to specify the author or maintainer of the image by setting the `Author` field in the generated image metadata.

```bash
MAINTAINER <name>
```

## LABEL
The `LABEL` instruction is used to attach metadata to an image.
Labels are cumulative, meaning those defines in base images using `FROM` are inherited

```bash
LABEL <key>=<value>
```

## ENV
The `ENV` instruction defines environment variables in the image.
These variables are available to all subsequent instructions in the Dockerfile and persist in any container created from the image and persist in any containers created from the image

```bash
ENV <key>=<value>
```

## ARG
The `ARG` instaruction declares build-time variables that can be passed to the Docker build process using the `--build-arg <varname>=<value>` flag

```bash
ARG <name>=<default value>
```

## WORKDIR
The `WORKDIR` instruction specifies the working directory for any subsequent `RUN`, `CMD`, `ENTRYPOINT`, `ADD` instructions in the Dockerfile

```bash
WORKDIR <path/to/workdir>
```

## ADD
The `ADD` instruction transfers files, directories, or remote file URLs from `<src>` and integrates them into the image's filesystem at the specified `<dest>` location.

```bash
ADD <src> <dest>
```

## COPY
The `COPY` instruction transfers files or directories from `<src>` and places them into the image's filesystem at the specified `<dest>` location.

```bash
COPY <src> <dest>
```

## RUN
The `RUN` instruction executes commands inside the container during the build process. It supports two forms: the shell form and the exec form.
- exec form: this avoids shell string manipulation, allowing you to run commands directly in an image that may not have the specified shell executable.
- shell form: This form runs the command in a shell (default is `/bin/sh -c` on linux)

```bash
RUN <command>
```

```bash
RUN ["<executable>", "<param1>", "<param2>"]
```

## CMD
The primary role of `CMD` instruction is to provide default behavior for an executing container. This can include specifying an executable or omitting it, in which case the `ENTRYPOINT` instruction must also be provided.
- *Single CMD*: A Dockerfile can only have one `CMD` instruction. If multiple `CMD` instructions are defined, only the last one will take effect.
- *Default for ENTRYPOINT*: If `CMD` is used to define default arguments for `ENTRYPOINT` instruction, both should be specified in JSON array format.
- *Overriding CMD*: Any arguments provided by ther user through the `docker run` command will override the defaults set by the `CMD`.

Exec form
```bash
CMD ["<executable>", "<param1>", "<param2>"]
```

As a default parameters for `ENTRYPOINT`
```bash
CMD ["<param1>", "<param2>"]
```

Shell form
```bash
CMD <executable> <param1> <param2>
```

## ENTRYPOINT
THe `ENTRYPOINT` instruction allows you to configure a container to run as an executable. When using the exec form of `ENTRYPOINT`, any command-line arguments passed through `docker run` will be appended after the defined executable and will override the elements specified in `CMD`

```bash
ENTRYPOINT ["<executable>", "<param1>, "<param2>"]
```

## EXPOSE
The `EXPOSE` instruction notifies Docker that the container will listen on the specified network port during runtime. However, it's important to note that using `EXPOSE` does not make the ports accessible to the host system.

```bash
EXPOSE <port> [<port> ..]
```

## VOLUME
Creates a mount point with the specific name and marks it as holding externally mounted volumes from native or other containers.

```bash
VOLUME <path> [<path> ..]
```

## USER
The `USER` instruction specifies the username or UID to be used when running the image, as well as for any subsequent `RUN`, `CMD` and `ENTRYPOINT` instructions in the Dockerfile

```bash
USER <username> | <UID>
```

## HEALTHCHECK
THe `HEALTHCHECK` instruction defines how Docker should test if a container is still functioning properly. When a health check is successful, the container is marked as healthy. If it fails consecutively a specific number of times, the container is marked as unhealthy.

The options available are:
- `--interval=<duration>`
- `--timeout=<duration>`
- `--retries=<number>`