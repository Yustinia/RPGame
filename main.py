# ================
# IMPORT LIBRARIES
# ================

import time
import random

# ======================
# IMPORT CHARACTER CLASS
# ======================

from character import Tank, Swordsman, Wizard, Elf, Dragon

# ===================
# INSTANTIATING CLASS
# ===================

dragon = Dragon("Draggin Yaface")

# ===========
# START GAME?
# ===========


def main():
    display_menu()
    choice = choose_action()

    if choice == "s":
        start_intro()
        battle(party, dragon)
    elif choice == "q":
        print("Exiting...")


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
        "Flames lick the sky as the dragon's roar shatters the silence.",
        "Sir Tanksalot plants his shield like a fortress, unyielding and resolute.",
        "Stabby McStabface tightens his grip, blades gleaming for the deadly dance.",
        "Spellbert Einstein murmurs incantations, weaving glowing shields and lightning speed.",
        "Florence NightingElf moves like a whisper, ready to mend wounds and steady hearts.",
        "Together they stand, a wall of iron, steel, magic, and hope against the beast.",
        "No fear, no falter — only the fierce will to survive the fiery storm.",
    ]

    for line in intro:
        print(line)
        print("=" * len(line))
        time.sleep(1)


party = [Tank("Sir Tanksalot"), Swordsman("Stabby McStabface"),
         Wizard("Spellbert Einstein"), Elf("Florence NightingElf")]


def battle(party, dragon):
    turn_index = 0  # start with the first hero

    while any(hero.get_hp() for hero in party) and dragon.get_hp() > 0:
        current_hero = party[turn_index]

        if current_hero.get_hp() > 0:
            print(f"{current_hero.name}'s Turn".center(100))
            print("[A]ttack [D]efend".center(100))

            # if ELF
            if isinstance(current_hero, Elf):
                print("[H]eal".center(100))

            # if WIZARD
            if isinstance(current_hero, Wizard):
                print("[B]uff".center(100))

            choice = input("> ").strip().lower()

            if choice == "a":
                damage = max(0, current_hero.get_atk_power() -
                             dragon.get_defence_str() // 10)
                dragon.hp -= damage
                print(
                    f"\n{current_hero.name} attacks {dragon.name} with {damage} damage!\n")

            elif choice == "d":
                block = current_hero.do_defend()
                print(
                    f"\n{current_hero.name} prepares to block {block} damage\n")
                current_hero.defending = True

            elif choice == "h" and isinstance(current_hero, Elf):
                # FULL PARTY HEAL
                print(
                    f"\n{current_hero.name} casts a healing spell on the whole party!\n")

                for ally in party:
                    if ally.get_hp() > 0:  # skip dead heroes
                        heal_amt = current_hero.do_heal()
                        ally.hp += heal_amt
                        print(
                            f"{ally.name} heals for {heal_amt}! (HP: {ally.get_hp()})")

            elif choice == "b" and isinstance(current_hero, Wizard):
                # FULL PARTY ATK BUFF
                print(f"{current_hero.name} casts a powerful buff on the party!")

                for ally in party:
                    if ally.get_hp() > 0:  # only buff living heroes
                        buff_amt = current_hero.do_buff()
                        ally.atk_power += buff_amt
                        print(
                            f"{ally.name}'s attack power increased by {buff_amt}! (ATK: {ally.get_atk_power()})")
            else:
                print(f"{current_hero.name} missed their opportunity")

        time.sleep(0.5)

        # === CHECK DRAGON STATE
        if dragon.get_hp() <= 0:
            print(f"The heroes won and slain {dragon.name}")
            break

        # === DRAGON TURN
        if turn_index == len(party) - 1:
            print(f"{dragon.name}'s Turn".center(100))
            target = random.choice(
                [hero for hero in party if hero.get_hp() > 0])

            block_pwr = target.do_defend() if getattr(target, "defending", False) else 0

            raw_damage = max(0, dragon.get_atk_power() -
                             target.get_defence_str() // 10)
            damage = max(0, raw_damage - block_pwr)

            target.hp -= raw_damage

            print(
                f"\n{dragon.name} attacks {target.name} for {raw_damage} damage!\n")

            if not any(hero.get_hp() > 0 for hero in party):
                print("The party has been wiped out...")
                break

        # Move to next hero turn
        current_hero.show_stats()
        print(f"Dragon HP: {dragon.get_hp()}")
        turn_index = (turn_index + 1) % len(party)
        time.sleep(0.5)


main()
