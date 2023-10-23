import asyncio

from pytgcalls import PyTgCalls, idle
from pytgcalls.types import (AudioImagePiped, AudioPiped, AudioVideoPiped,
                             LowQualityVideo, VideoPiped)
from rich.console import Console
from telethon import utils
from youtube_dl import YoutubeDL

from functions.base import TelethonFunction

console = Console()


class VoicePlayFunc(TelethonFunction):
    """Join voice chat and play audio"""

    async def join_and_play(self, session):
        await session.start()

        app = PyTgCalls(session)
        await app.start()
        entity = await session.get_entity(self.chat)

        if self.format_choice == "1":
            await app.join_group_call(
                utils.get_peer_id(entity),
                AudioPiped(self.media_url),
            )
        
        elif self.format_choice == "2":
            await app.join_group_call(
                utils.get_peer_id(entity),
                AudioVideoPiped(self.media_url, video_parameters=LowQualityVideo())
            )

        await idle()


    async def execute(self):
        self.ask_accounts_count()

        self.chat = console.input("[bold red]chat link> [/]")

        console.print(
            "\n[bold white][1] Audio\n"
            "[2] Video\n"
        )

        self.format_choice = console.input("[bold white]>> [/]")
        
        console.print(
            "\n[bold white][1] From Youtube\n"
            "[2] From direct link to file[/]\n"
        )

        source_choice = console.input("[bold white]>> [/]")

        if source_choice == "1":
            url = console.input("[bold red]video url> [/]")
            ydl = YoutubeDL()

            r = ydl.extract_info(url, download=False)

            if self.format_choice == "1":
                for rformat in r["formats"]:
                    if rformat["fps"] is None:
                        self.media_url = rformat["url"]
                        break
            
            elif self.format_choice == "2":
                self.media_url = r["formats"][-1]["url"]
        
        elif source_choice == "2":
            self.media_url = console.input("[bold red]media url> [/]")

        await asyncio.gather(*[
            self.join_and_play(session)
            for session in self.sessions
        ])
