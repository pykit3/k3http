"""
k3http is utility to .

Execute a shell script::

    import k3http

    # execute a shell script

    returncode, out, err = pk3proc.shell_script('ls / | grep bin')
    print returncode
    print out
    # output:
    # > 0
    # > bin
    # > sbin

Run a command::

    # Unlike the above snippet, following statement does not start an sh process.
    returncode, out, err = pk3proc.command('ls', 'a*', cwd='/usr/local')

"""

# from .proc import CalledProcessError
# from .proc import ProcError

__version__ = "0.1.0"
__name__ = "k3http"

from .k3http import foo
from .k3http import SomeError