from pathlib import Path
import shutil

from fire import Fire


def copy_files(src_dir, dest_dir):
    src_path = Path(src_dir)
    dest_path = Path(dest_dir)

    # ディレクトリが存在しない場合は作成
    dest_path.mkdir(parents=True, exist_ok=True)

    for item in src_path.iterdir():
        item_dest = dest_path / item.name

        if item.is_dir():
            # サブディレクトリの場合は再帰的にコピー
            shutil.copytree(item, item_dest)
        else:
            # ファイルの場合はコピー
            shutil.copy2(item, item_dest)


def cli(target: str):
    _target = Path.cwd() / target
    _target = _target.absolute()
    if _target.exists():
        raise FileExistsError("distination directory exists", str(_target))

    assets = (Path(__file__).parent / "assets").absolute()
    copy_files(assets, _target)


def main_cli():
    Fire(cli)


if __name__ == "__main__":
    main_cli()
