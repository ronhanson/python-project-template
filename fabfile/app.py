from fabric.decorators import task
from fabric.colors import cyan, red
from fabric.api import local


@task
def clean():
    """Clean pyc files from project folder"""
    print(cyan('Cleaning .pyc files...'))
    local('find . -name "*.pyc" -exec rm -rf {} \\;')

