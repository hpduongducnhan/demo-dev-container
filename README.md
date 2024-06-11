# Dev container demo
1. Requirement
    - [Requirements from website](https://code.visualstudio.com/docs/devcontainers/containers#_getting-started)

2. Create devcontainer.json file
    ``` bash
    .
    ├── .devcontainer
    │   └── devcontainer.json
    │
    │   ....
    │
    ├── poetry.lock
    ├── pyproject.toml
    └── README.md
    ```

3. Select templates (optional)
    - [Reference this link](https://github.com/devcontainers/templates)

4. Select container image from this repository
    - [Vscode Devcontainer Github](https://github.com/devcontainers)
    - [Python Images](https://github.com/devcontainers/images/tree/main/src/python) - should use python version >= 3.10 for long term support and new features
        - mcr.microsoft.com/devcontainers/python:3.12
        - mcr.microsoft.com/devcontainers/python:3.11
        - mcr.microsoft.com/devcontainers/python:3.10
        - ...
        - mcr.microsoft.com/devcontainers/python:1.0.0-3.10
        - mcr.microsoft.com/devcontainers/python:1.0.0-3.10-bullseye
        - mcr.microsoft.com/devcontainers/python:1.0.0-3.10-buster 

    -> 
    ``` .devcontainer.json
    {
        ...
        "image": "mcr.microsoft.com/devcontainers/python:3.12",
        ...
    }
    ```

5. Using your own image
    - A sample Docker file to build image with debug tools (base on python image - OS Debian)
    - [Docker Python images](https://hub.docker.com/_/python/tags). Select specific tag, for example: python:3.12.3-slim-bullseye
        ``` Dockerfile
        FROM python:3.12.3-slim-bullseye
        #ENV http_proxy http://proxy.hcm.fpt.vn:80              # proxy if you need
        #ENV https_proxy http://proxy.hcm.fpt.vn:80             # proxy if you need
        #ENV no_proxy=localhost,127.0.0.1,::1,172.24.222.112    # proxy if you need
        RUN apt-get update -y
        RUN apt-get install -y --no-install-recommends \
            make gcc \
            build-essential python-dev \
            libffi-dev libheif-dev libde265-dev libpq-dev \
            libxml2-dev libxmlsec1-dev \
            ffmpeg mime-support \
            telnet iputils-ping curl vim procps net-tools htop \          
            && rm -rf /var/lib/apt/lists/*
        
        # setup working directory
        WORKDIR /app

        # image already has pip3, if not work, change to pip or pip3.x (x is python version - pip3.12)
        # install poetry 
        RUN pip3 install --upgrade pip \
            && pip3 install poetry wheel \
            && poetry config virtualenvs.in-project true
        ```
    - Config to selec this Dockerfile
    
    -> 
    ``` .devcontainer.json
    {
        ...
        "build": {
            "dockerfile": "../Dockerfile"           
        },
        ...

        // using "../" because devcontainer.json in .devcontainer directory and Dockerfile in root directory
    }
    ```

6. Configure
    - Forward port to make ports available locally
        ``` .devcontainer.json
        {
            "forwardPorts": [5000, 5001]
        }
        ```

    - Map port with host, allow access from outside
        ``` .devcontainer.json
        {
            "runArgs": [
                "-p", "5001:5001",
                "-p", "5002:5002"
            ],
        }
        ```
    - Mount volume
        ``` .devcontainer.json
        {
            "runArgs": [
                "-v", "path/to/volume:path/to/volume"
            ],
        }
        ```

7. Add extra feature you need
    - Development Container 'Features': A set of simple and reusable Features. Quickly add a language/tool/CLI to a development container.
    - [Github Devcontainer features ](https://github.com/devcontainers/features/)
    - [Devcontainer Features for Python](https://github.com/devcontainers/features/tree/main/src/python)
    
8. Extension - make devcontainer is the same local vscode
    - Main extension for python developer
        ``` .devcontainer.json
        {
            "customizations": {
                "vscode": {
                    "extensions": [
                        "ms-python.python",
                        "ms-python.vscode-pylance",
                        "ms-python.autopep8"
                    ]
                }
            }
        }
        ```

9. Specific settings for contnainer
    - [Dev Container Specification](https://containers.dev/implementors/json_reference/)
    - Add proxy for container
        ``` .devcontainer.json
        {
            "containerEnv": {
                "http_proxy": "http://proxy.fpt.vn:80",
                "https_proxy": "http://proxy.fpt.vn:80",
                "no_proxy": "localhost,127.0.0.1"
            }
        }
        ```
    - Using default terminal is bash shell 
        ``` .devcontainer.json
        {
            "customizations": {
                "vscode": {
                    "settings": {
                        "terminal.integrated.shell.linux": "/bin/bash"
                    }
                }
            }
        }
        ```
    - [Lifecycle scripts](https://containers.dev/implementors/json_reference/#lifecycle-scripts)
        - postStartCommand: command to run each time the container is successfully started.
        ``` .devcontainer.json
        {
            "postStartCommand": "cd /workspaces/<your-root-directory> && poetry install" 
        }
        ```

10. Handle error: current user does not have permission to run Docker
    - Provide permission to user, run directly on remote machine where docker engine is running on
        ``` /bin/bash
        $ sudo groupadd docker
        $ sudo usermod -aG docker $USER
        $ newgrp docker

        testing
        $ docker run hello-world
        
        ```
    - Close all open terminal then reload the vscode by ctrl + shift + P -> reload window
    - If still get error
        ```
        WARNING: Error loading config file: /home/user/.docker/config.json -
        stat /home/user/.docker/config.json: permission denied
        ```
        Send command
        ```
        $ sudo chown "$USER":"$USER" /home/"$USER"/.docker -R
        $ sudo chmod g+rwx "$HOME/.docker" -R
        ```