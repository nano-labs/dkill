# dkill - Docker kill
Command to easily select docker containers to kill

![Usage gif](https://github.com/nano-labs/dkill/blob/main/imgs/dkill.gif)

## Install
```
pip3 install dkill
```

## Usage
```shell
> dkill
```
- SPACEBAR to select containers
- ENTER to kill selected containers

## How does it work
It uses `docker ps` command to list all running container then `docker kill <CONTAINER IDs>` to kill them