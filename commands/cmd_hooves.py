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
#  Ported to Python by Davion of MudBytes.net using Miniboa
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

import handler_game
import interp
import merc


# noinspection PyUnusedLocal
def cmd_hooves(ch, argument):
    if ch.is_npc():
        return

    if not ch.is_demon():
        ch.huh()
        return

    if not ch.dempower.is_set(merc.DEM_HOOVES):
        ch.send("You haven't been granted the gift of horns.\n")
        return

    ch.demaff.tog_bit(merc.DEM_HOOVES)
    if ch.demaff.is_set(merc.DEM_HOOVES):
        ch.send("Your feet transform into hooves.\n")
        handler_game.act("$n's feet transform into hooves.", ch, None, None, merc.TO_ROOM)
    else:
        ch.send("Your hooves transform into feet.\n")
        handler_game.act("$n's hooves transform back into $s feet.", ch, None, None, merc.TO_ROOM)


interp.register_command(
    interp.CmdType(
        name="hooves",
        cmd_fun=cmd_hooves,
        position=merc.POS_STANDING, level=3,
        log=merc.LOG_NORMAL, show=True,
        default_arg=""
    )
)
