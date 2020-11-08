
#    Copyright (C) Ayush Sharma
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
# 
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.

import inspect
import logging
import re
from pathlib import Path
import functools
from telethon import events
from chatrobot import chatbot
from chatrobot import Config
import glob
bothandler = Config.COMMAND_HAND_LER
def chatbot_cmd(add_cmd, is_args=False):
    def cmd(func):
        if is_args:
            pattern = bothandler + add_cmd + "(?: |$)(.*)"
        else:
            pattern = bothandler + add_cmd + "$"
        chatbot.add_event_handler(
            func, events.NewMessage(incoming=True, pattern=pattern)
        )

    return cmd

def god_only():
    def decorator(func):
        @functools.wraps(func)
        async def wrapper(event):
            moms = Config.OWNER_ID
            if event.sender_id == moms:
                await func(event)
            else:
                pass

        return wrapper

    return decorator

def start_chatbot(shortname):
    if shortname.startswith("__"):
        pass
    elif shortname.endswith("_"):
        import importlib
        import sys
        from pathlib import Path
        import chatrobot.utils
        path = Path(f"chatrobot/plugins/{shortname}.py")
        name = "chatrobot.plugins.{}".format(shortname)
        spec = importlib.util.spec_from_file_location(name, path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        print("Starting Your Assistant Bot.")
        print("Assistant Sucessfully imported " + shortname)
    else:
        import importlib
        import sys
        from pathlib import Path
        import chatrobot.utils
        path = Path(f"chatrobot/plugins/{shortname}.py")
        name = "chatrobot.plugins.{}".format(shortname)
        spec = importlib.util.spec_from_file_location(name, path)
        mod = importlib.util.module_from_spec(spec)
        mod.chatbot_cmd = chatbot_cmd
        mod.chatbot = chatbot
        mod.Config = Config
        mod.god_only = god_only()
        spec.loader.exec_module(mod)
        sys.modules["chatrobot.plugins" + shortname] = mod
        print("Assistants Has imported " + shortname)
