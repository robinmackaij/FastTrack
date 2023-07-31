# pylint: disable=missing-function-docstring, missing-module-docstring, unused-argument
import pathlib
import subprocess

from invoke import Context, task

ROOT = pathlib.Path(__file__).parent.resolve().as_posix()


@task
def start_api(context: Context) -> None:
    cmd = [
        "python",
        "-m",
        "uvicorn",
        "demo_api.main:api",
        f"--app-dir {ROOT}/src/demo_api",
        "--host 0.0.0.0",
        "--port 8000",
        "--reload",
        f"--reload-dir {ROOT}/src/demo_api",
        f"--log-config {ROOT}/uvicorn_log_config.yaml",
    ]
    subprocess.run(" ".join(cmd), shell=True, check=False)


@task
def run_tests(context: Context) -> None:
    cmd = [
        "python",
        "-m",
        "robot",
        f"--variable=ROOT:{ROOT}",
        f"--outputdir={ROOT}/logs",
        "--loglevel=TRACE:TRACE",
        f"{ROOT}/RobotFrameworkUnleashed/suites",
    ]
    subprocess.run(" ".join(cmd), shell=True, check=False)


@task
def type_check(context: Context) -> None:
    subprocess.run(f"mypy {ROOT}/src", shell=True, check=False)
    subprocess.run(f"pyright {ROOT}/src", shell=True, check=False)


@task
def lint(context: Context) -> None:
    subprocess.run(f"ruff {ROOT}", shell=True, check=False)
    subprocess.run(f"pylint {ROOT}/src/demo_api", shell=True, check=False)
    subprocess.run(f"robocop {ROOT}", shell=True, check=False)


@task
def format_code(context: Context) -> None:
    subprocess.run(f"black {ROOT}", shell=True, check=False)
    subprocess.run(f"isort {ROOT}", shell=True, check=False)
    subprocess.run(f"robotidy {ROOT}", shell=True, check=False)
