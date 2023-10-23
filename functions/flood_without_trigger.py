import asyncio
from functions.base import TelethonFunction
from functions.flood import Flood
from rich.console import Console

console = Console()


class FloodWithoutTriggerFunc(TelethonFunction):
    """Flood without trigger (asyncio)"""

    async def execute(self):
        link = console.input("[bold red]link> [/]")
        flood = Flood(self.storage, self.settings)
        flood.ask()

        await asyncio.gather(*[
            flood.flood(session, link, flood.function)
            for session in self.sessions
        ])
        