import asyncio
import random

from pyrogram import Client
from functions.base import PyrogramFunction
from rich.console import Console

console = Console()


class ReactionsFunc(PyrogramFunction):
    """Set reactions to message/post"""

    reactions = ['👍', '❤️', '🔥', '🥰', '👏', '😁', '🎉', '🤩', '👎', '🤯', '😱', '🤬', '😢', '🤮', '💩', '🙏']

    async def set_reaction(self, session: Client, chat_username: str, message_id: int, reaction=None):
        if not reaction:
            reaction = random.choice(self.reactions)

        async with session:
            try:
                await session.send_reaction(
                    chat_id=chat_username,
                    message_id=int(message_id),
                    emoji=reaction 
                )
            except Exception as err:
                console.print(f"[bold red][ERROR][/] [bold yellow][{session.me.id}][/] : {err}")
            else:
                console.print(f"[bold green][SUCCESS] [{session.me.id}][/] : Reaction \"{reaction}\" was sent")


    async def execute(self):
        link_to_message = console.input("[bold red]link to msg/post> [/]")
        chat_username, message_id = link_to_message.split("/")[-2:]

        reaction = console.input(
            "[bold red]enter reaction ({reactions}) or skip for random> [/]"
            .format(reactions=", ".join(self.reactions))
        )

        await asyncio.gather(*[
            self.set_reaction(
                session=session,
                chat_username=chat_username,
                message_id=message_id,
                reaction=reaction
            )
            for session in self.sessions
        ])
