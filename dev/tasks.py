from invoke import task
from pathlib import Path


PROJECT_PATH = Path(__file__).parents[1]
TEST_FOLDER = PROJECT_PATH / "tests"
VENV = PROJECT_PATH / "venv/bin/"
PY = VENV / "python"


@task()
def typing(c):
    c.run("mypy --config-file .mypy.ini")


@task()
def test(c, files="*.py"):
    for file_name in TEST_FOLDER.glob(files):
        c.run(f"{PY} {file_name}")