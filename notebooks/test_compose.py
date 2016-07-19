# -*- coding: utf-8 -*-

"""

Testing compose commands from python

"""

class mem:
    pass

#############################
# from __future__ import absolute_import

from compose.cli.main import TopLevelCommand
from compose.cli.command import project_from_options
import compose.cli.errors as errors
from compose.cli.docopt_command import DocoptDispatcher


#############################

def compose_com(cli_options):

    dispatcher = DocoptDispatcher(
        TopLevelCommand,
        {'options_first': True, 'version': '1.7.1'})

    options, handler, command_options = dispatcher.parse(cli_options)

    # print("TEST", options, handler, command_options)
    # exit(1)

    project = project_from_options('.', options)
    mem.current_project = project

    command = TopLevelCommand(project)

    with errors.handle_connection_errors(project.client):
        out = handler(command, command_options)
        print("Launched command, with output:\n", out)
    return out


import contextlib
import sys

try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO


@contextlib.contextmanager
def nostdout():
    save_stdout = sys.stdout
    sys.stdout = StringIO()
    sys.stderr = StringIO()
    yield
    sys.stdout = save_stdout

#############################

# Launch a ps empty command just to save the project
with nostdout():
    compose_com(['ps'])

# use the current project to list services
for service in mem.current_project.services:
    print("SERVICE", service)

## TO BE REMOVED
exit(0)

compose_com(['up', '-d', 'graphdb'])
compose_com(['ps'])
