#  PythonWars copyright © 2020 by Paul Penner. All rights reserved. In order to
#  use this codebase you must comply with all licenses.
#
#  Original Diku Mud copyright © 1990, 1991 by Sebastian Hammer,
#  Michael Seifert, Hans Henrik Stærfeldt, Tom Madsen, and Katja Nyboe.
#
#  Merc Diku Mud improvements copyright © 1992, 1993 by Michael
#  Chastain, Michael Quan, and Mitchell Tse.
#
#  GodWars improvements copyright © 1995, 1996 by Richard Woolcock.
#
#  ROM 2.4 is copyright 1993-1998 Russ Taylor.  ROM has been brought to
#  you by the ROM consortium:  Russ Taylor (rtaylor@hypercube.org),
#  Gabrielle Taylor (gtaylor@hypercube.org), and Brian Moore (zump@rom.org).
#
#   Ported to Python by Davion of MudBytes.net using Miniboa
#  (https://code.google.com/p/miniboa/).
#
#  In order to use any part of this Merc Diku Mud, you must comply with
#  both the original Diku license in 'license.doc' as well the Merc
#  license in 'license.txt'.  In particular, you may not remove either of
#  these copyright notices.
#
#  Much time and thought has gone into this software, and you are
#  benefiting.  We hope that you share your changes too.  What goes
#  around, comes around.

import game_utils
import handler_game
import interp
import merc


# New routines by Dionysos.
def cmd_invis(ch, argument):
    # RT code for taking a level argument
    argument, arg = game_utils.read_word(argument)

    if not arg:
        if ch.invis_level:
            ch.invis_level = 0
            handler_game.act("$n slowly fades into existence.", ch, None, None, merc.TO_ROOM)
            ch.send("You slowly fade back into existence.\n")
        else:
            ch.invis_level = ch.trust
            handler_game.act("$n slowly fades into thin air.", ch, None, None, merc.TO_ROOM)
            ch.send("You slowly vanish into thin air.\n")
    else:
        # do the level thing
        level = int(arg) if arg.isdigit() else -1
        if level not in merc.irange(2, ch.trust):
            ch.send("Invis level must be between 2 and your level.\n")
            return

        ch.reply = None
        ch.invis_level = level
        handler_game.act("$n slowly fades into thin air.", ch, None, None, merc.TO_ROOM)
        ch.send("You slowly vanish into thin air.\n")


interp.register_command(
    interp.CmdType(
        name="invis",
        cmd_fun=cmd_invis,
        position=merc.POS_DEAD, level=7,
        log=merc.LOG_NORMAL, show=True,
        default_arg=""
    )
)
