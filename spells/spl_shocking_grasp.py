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

import const
import fight
import game_utils
import handler_magic
import merc


# noinspection PyUnusedLocal
def spl_shocking_grasp(sn, level, ch, victim, target):
    dam_each = [10, 10, 10, 15, 15, 15, 20, 20, 25, 29, 33, 36, 39, 39, 39, 40,
                40, 41, 41, 42, 42, 43, 43, 44, 44, 45, 45, 46, 46, 47, 47, 48,
                48, 49, 49, 50, 50, 51, 51, 52, 52, 53, 53, 54, 54, 55, 55, 56,
                56, 57, 57, 60, 70, 85, 100, 125, 150, 175, 200, 225, 300]

    if victim.itemaff.is_set(merc.ITEMA_SHOCKSHIELD):
        return

    level = min(level, len(dam_each) - 1)
    level = max(0, level)
    dam = game_utils.number_range(dam_each[level] // 2, dam_each[level] * 2)

    if handler_magic.saves_spell(level, victim):
        dam //= 2

    fight.damage(ch, victim, 0 if (not victim.is_npc() and victim.immune.is_set(merc.IMM_LIGHTNING)) else dam, sn)


const.register_spell(
    const.skill_type(
        name="shocking grasp",
        skill_level=99,
        spell_fun=spl_shocking_grasp,
        target=merc.TAR_CHAR_OFFENSIVE,
        minimum_position=merc.POS_FIGHTING,
        pgsn=None,
        slot=const.slot(37),
        min_mana=15,
        beats=12,
        noun_damage="shocking grasp",
        msg_off="!Shocking Grasp!"
    )
)
