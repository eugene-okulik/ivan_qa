from rich import print
from rich.tree import Tree
import os


# функция для добавления папок в дерево
def add_folder_to_tree(tree, path):
    with os.scandir(path) as items:
        for item in sorted(items, key=lambda e: e.name.lower()):
            if item.is_dir():
                branch = tree.add(
                    f":open_file_folder: [bold blue]{item.name}[/bold blue]"
                )
                add_folder_to_tree(branch, item.path)  # рекурсия
            else:
                tree.add(
                    f":page_facing_up: [bold green]{item.name}[/bold green]"
                )


# функция для проверки наличия файла или папки и отрисовки дерева папок
def check_file_or_folder(path):
    if not os.path.exists(path):
        print(f":cross_mark: [red]Файл или папка {path} не найдены[/red]\n")
        return None

    if os.path.isfile(path):
        print(
            f":page_facing_up: [bold green]Файл"
            f"{os.path.basename(path)} найден[/bold green]\n"
        )
        return "file", path

    tree = Tree(
        f":open_file_folder: [bold yellow]Папка {path}"
        f"найдена[/bold yellow]"
    )
    add_folder_to_tree(tree, path)
    print(tree)
    print()

    return "folder", path
