<img src="/artwork/CACAO-Roaster-logo.jpg" alt="CACAO Roaster logo" width="400"/>

**Online Instance:**[ https://mateusdz.github.io/AInception-roaster/](https://mateusdz.github.io/AInception-roaster/)

# CACAO Roaster Sub-Project

# Getting Started

These instructions will get you a copy of the project up and running on your local machine for development purposes. See deployment for notes on how to deploy the project on a live system.

## Installation

- Make sure you have [Docker](https://www.docker.com/) installed on your PC.
- The first command after you clone the project is to build the node modules. The docker command is `docker run -it -v ./code:/application node:21.6-alpine3.19 /bin/sh -c "cd /application && npm install"`. Make sure to be on the root of the cloned repository in order to find the `code` folder to mount.
- If the above command finishes successfully, navigate to docker folder and do `docker compose up -d`. This will build the whole project and run it locally.

When you are done with the above, the below URLs will be available:

| Name          | URL                            |
| ------------- | ------------------------------ |
| Cacao Roaster UI       | https://cacao-roaster.traefik.me/   |
| Soarca       | https://cacao-roaster-soarka.traefik.me/   |
| Webshell For a POC         | https://cacao-roaster-webshell-exploit.traefik.me/         |


**Building the project for production**

Use the below docker command to build it for production:
```
docker run -it -v ./code:/application node:21.6-alpine3.19 /bin/sh -c "cd /application && npm run build
```

## Deployment

Install serve service on hosting machine

```
npm install serve
```

Host production bundle

```
serve dist
```

Or use [Docker](https://www.docker.com/) to spin up a fully functioning container

```
docker build -t cacao-roaster .
docker run -it -p 3000:3000 cacao-roaster
```
