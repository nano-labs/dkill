#!/usr/bin/env python3.8
"""Simple menu to kill docker containers."""
import subprocess
from bullet import Check

running_services = {}
docker_ps = subprocess.run(
    ["docker", "ps", "--format", "'{{json .Names }}:{{json .ID}}'"], capture_output=True
).stdout.decode()
for s in docker_ps.replace('"', '').replace("'", "").split("\n"):
    if not s:
        continue
    name, container_id = s.split(":")
    running_services[name] = container_id

services = sorted(list(running_services.keys()))
if not services:
    print("No containers running. Come back later")
else:
    cli = Check(prompt="Check which containers you want to kill", check="> ", choices=services)
    result = cli.launch()
    ids = [running_services[r] for r in result]
    print(subprocess.run(['docker', 'kill'] + ids, capture_output=True).stdout.decode())
