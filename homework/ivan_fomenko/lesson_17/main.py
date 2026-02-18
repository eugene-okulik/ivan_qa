import argparse
from rich import print
from check_file_or_folder import check_file_or_folder
from search_utils import search_in_files
import os


parser = argparse.ArgumentParser()
parser.add_argument('file', type=str, help='File name')
parser.add_argument(
    '-t', '--text', type=str, required=True, help='Text for search in file'
)


# вынес аргументы в переменные для удобства
args = parser.parse_args()
user_path = args.file
user_text = args.text


# пишем где и что ищем
print(f'{"="*60}\n'
      f'Ищем текст "{user_text}" в файле "{user_path}"\n',
      f'{"="*60}')


# проверяем наличие файла или папки и отрисовываем дерево папок
obj_type, path = check_file_or_folder(user_path)


# папку читаем - ищем текст в каждом файле папки
if obj_type == "file":
    search_in_files(user_path, user_text)

elif obj_type == "folder":
    print(
        f":mag_right: [bold blue]Ищем текст в файлах папки {user_path}"
        f"...[/bold blue]\n"
    )
    for root, dirs, files in os.walk(user_path):
        for file in files:
            file_path = os.path.join(root, file)
            search_in_files(file_path, user_text)
