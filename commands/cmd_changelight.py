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
import merc


# noinspection PyUnusedLocal
def cmd_changelight(ch, argument):
    ch.in_room.room_flags.tog_bit(merc.ROOM_DARK)
    if ch.in_room.room_flags.is_set(merc.ROOM_DARK):
        handler_game.act("The lights in the room suddenly go out!", ch, None, None, merc.TO_CHAR)
        handler_game.act("The lights in the room suddenly go out!", ch, None, None, merc.TO_ROOM)
    else:
        handler_game.act("The room is suddenly filled with light!", ch, None, None, merc.TO_CHAR)
        handler_game.act("The room is suddenly filled with light!", ch, None, None, merc.TO_ROOM)
