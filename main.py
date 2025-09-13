# ================
# IMPORT LIBRARIES
# ================

import time

# ======================
# IMPORT CHARACTER CLASS
# ======================

from character import Tank, Dragon

# ===================
# INSTANTIATING CLASS
# ===================

tank = Tank("Sir Tanksalot")
dragon = Dragon("Draggin Yaface")


# ===========
# START GAME?
# ===========

def display_menu():
    intro = [
        "Welcome.. I have no idea what to put here yet",
        "[S]tart",
        "[Q]uit",
    ]

    for line in intro:
        print(line)
        print("=" * len(line))
        time.sleep(0.5)


def choose_action():
    while True:
        choice = input("> ").strip().lower()

        if choice == "s":
            print("Starting game...")

            for seconds in range(3, 0, -1):
                print(seconds)
                time.sleep(1)

            break

        elif choice == "q":
            break

        elif not choice:
            print("Entry cannot be empty")

        else:
            print("Invalid")

    return choice


def start_intro():
    intro = [
        "The ground trembles.",
        "The dragon descends, fiery breath scorching the sky.",
        "The tank steps forward, armor gleaming with unyielding steel.",
        "Shield raised, heart pounding with battle fury.",
        "Eye to eye with the beast—no retreat, no fear.",
        "Iron will clashes with blazing fury.",
        "Only one will stand victorious.",
    ]

    for line in intro:
        print(line)
        print("=" * len(line))
        time.sleep(0.5)


def start_battle(tank, dragon):
    while tank.get_hp() > 0 and dragon.get_hp() > 0:
        # === player input
        moves = [
            "YOUR MOVE",
            "[A]ttack",
            "[D]efend",
            "[H]eal",
        ]

        for line in moves:
            print(line)
            time.sleep(0.5)

        choice = input("> ").strip().lower()

        if choice == "a":
            # tank attack
            damage = max(0, tank.get_atk_power() -
                         dragon.get_defence_str() // 10)
            dragon.hp -= damage
            print(f"{tank.name} attacks {dragon.name} with {damage} damage!\n")

        elif choice == "d":
            # === tank defend
            block_pwr = tank.do_defend()
            print(f"{tank.name} blocks {block_pwr} damage from {dragon.name}\n")

        elif choice == "h":
            # === tank heals
            heal_got = tank.do_heal()
            tank.hp = tank.get_hp() + heal_got
            print(f"{tank.name} healed {heal_got}. Health: {tank.get_hp()}\n")

        print(f"Dragon Health: {dragon.get_hp()}\n")
        time.sleep(1)

        # === Check dragon state
        if dragon.get_hp() <= 0:
            print(f"{tank.name} wins!\n")
            break

        # === Dragon Turn ===
        raw_damage = max(0, dragon.get_atk_power() -
                         tank.get_defence_str() // 10)
        damage = max(0, raw_damage - (block_pwr if choice == "d" else 0))

        tank.hp -= damage
        print(f"{dragon.name} attacks {tank.name} with {damage} damage!\n")
        print(f"Tank Health: {tank.get_hp()}\n")
        time.sleep(1)

        # === check tank state
        if tank.get_hp() <= 0:
            print(f"{tank.name} lost...\n")
            break


start_battle(tank, dragon)
