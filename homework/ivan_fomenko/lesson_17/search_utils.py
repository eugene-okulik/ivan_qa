from rich import print
from rich.panel import Panel
from rich.console import Console
import os

# консоль для красивого вывода
console = Console()


# функция для вырезания контекста вокруг найденного слова
def extract_context(line, text):
    words = line.strip().split()
    text_lower = text.lower()

    for i, word in enumerate(words):
        if text_lower in word.lower():
            start = max(0, i - 5)
            end = min(i + 6, len(words))
            context = words[start:end]

            context = words[start:end]

            highlighted_context = [
                f"[bold red]{w}[/bold red]" if text_lower in w.lower() else w
                for w in context
            ]
            return ' '.join(highlighted_context)


# функция для поиска текста и даты в файлах
def search_in_files(file_path, text):
    if text is None:
        print("[red]Текст для поиска не указан[/red]")
        return

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                if text.lower() in line.lower():
                    # фиксируем строку
                    # и выводим контекст вокруг найденного слова
                    words_line = line.strip().split()

                    # определяем позицию слова
                    for i, word in enumerate(words_line):
                        if text.lower() in word.lower():

                            context = extract_context(line, text)

                            if context:
                                file_name = os.path.basename(file_path)
                                panel_title = f"[blue]{file_name}[/blue]"
                                console.print(
                                    Panel(
                                        context,
                                        title=panel_title,
                                        border_style="blue",
                                        expand=False
                                    )
                                )
    except Exception as e:
        print(f":cross_mark: [red]Ошибка при чтении файла: {e}[/red]")
