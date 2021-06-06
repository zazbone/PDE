from invoke import task
from pathlib import Path
import toml


settings = toml.load("settings.toml")
TEST_FOLDER = Path(settings["project"]["test_path"])
PY = Path(settings["python_bin"]["py"])


@task()
def typing(c):
    c.run("mypy --config-file .mypy.ini")


@task()
def test(c, files="*.py"):
    for file_name in TEST_FOLDER.glob(files):
        c.run(f"{PY} {file_name}")