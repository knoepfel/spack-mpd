import shutil
import subprocess
from pathlib import Path

from .config import mpd_packages, rm_config, project_config
from .preconditions import preconditions, State


SUBCOMMAND = "rm-project"
ALIASES = ["rm"]


def setup_subparser(subparsers):
    rm_proj_description = """remove MPD project

Removing a project will:

  * Remove the project entry from the list printed by 'spack mpd list'
  * Delete the 'build' and 'local' directories
  * Uninstall the project's environment"""
    rm_proj = subparsers.add_parser(
        SUBCOMMAND, description=rm_proj_description, aliases=ALIASES, help="remove MPD project"
    )
    rm_proj.add_argument("project", metavar="<project name>", help="MPD project to remove")
    rm_proj.add_argument(
        "-f",
        "--force",
        action="store_true",
        help="remove project even if it is selected (environment must be deactivated)",
    )


def _run_no_output(*args):
    return subprocess.run(args, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


def _rm_packages(name):
    packages_path = Path(mpd_packages())
    if not packages_path.exists():
        return

    shutil.rmtree(packages_path / f"{name}-bootstrap", ignore_errors=True)


def rm_project(name, config):
    _run_no_output("spack", "env", "rm", "-y", name)
    _rm_packages(name)
    shutil.rmtree(config["build"], ignore_errors=True)
    shutil.rmtree(config["local"], ignore_errors=True)
    rm_config(name)


def process(args):
    if args.force:
        preconditions(State.INITIALIZED, ~State.ACTIVE_ENVIRONMENT)
    else:
        preconditions(State.INITIALIZED, ~State.SELECTED_PROJECT, ~State.ACTIVE_ENVIRONMENT)

    config = project_config(args.project)
    rm_project(args.project, config)
