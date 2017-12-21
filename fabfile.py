import pwd

import os
from fabric.decorators import task
from fabric.operations import local


@task
def mypy() -> None:
    """Run static analysis."""
    local('mypy --config-file mypy.ini .')


@task
def run() -> None:
    username: str = pwd.getpwuid(os.getuid())[0]
    local('rm -rf output')
    local('docker-compose up')
    local(f'sudo chown -R {username}:{username} output')
