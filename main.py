import sys
import locale
from rich.console import Console
from modules import updater
from modules.settings import Settings
from modules.storages.sessions_storage import SessionsStorage
from modules.storages.functions_storage import FunctionsStorage

console = Console()

console.print("""
[bold magenta]Copyright (C) 2023  @EverettHugh (TG)[/]
""")

console.print("Author: [link=https://t.me/EverettHugh]https://t.me/EverettHugh")


if "UTF-8" not in locale.getlocale():
    console.print("[bold yellow]WARNING:[/] You don't have UTF-8 encoding. Botnet may not work")

if sys.version_info < (3, 10, 0):
    console.print("\n[red]Error: you using an outdated Python version. Install Python 3.10.0 at least.")
else:
    if sys.platform == "win32":
        console.print("[yellow]Warning: you using an untested platform. Some features may not work properly\n")

    settings = Settings()

    sessions_storage = SessionsStorage(
        "sessions",
        settings.api_id,
        settings.api_hash
    )

    functions_storage = FunctionsStorage(
        "functions",
        sessions_storage,
        settings
    )

    console.print("[bold white]accounts count> %d[/]" % len(sessions_storage))

    for index, module in enumerate(functions_storage.functions):
        instance, doc = module

        console.print(
            "[bold white][{index}] {doc}[/]"
            .format(index=index + 1, doc=doc)
        )

    while True:
        console.print()

        try:
            choice = console.input(
                "[bold white]>> [/]"
            )

            while not choice.isdigit():
                choice = console.input(
                    "[bold white]>> [/]"
                )
        except KeyboardInterrupt:
            console.print("[bold white]Bye![/]")
            break

        else:
            choice = int(choice) - 1

        try:
            functions_storage.execute(choice)
        except KeyboardInterrupt:
            pass

