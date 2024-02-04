from pathlib import Path
from shutil import copytree,copy

from fire import Fire


def cli(target: str):
    _target = Path.cwd() / target
    _target = _target.absolute()
    if _target.exists():
        raise FileExistsError("distination directory exists", str(_target))

    assets = (Path(__file__).parent / "assets").absolute()
    print(assets)
    print(_target)
    print(copy(assets, _target))


def main_cli():
    Fire(cli)


if __name__ == "__main__":
    main_cli()
