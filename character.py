import random


class Character:
    def __init__(self, name):
        self.name = name
        self.hp = 5000
        self.atk_power = 1000
        self.defence_str = 1000
        self.crt_chance = random.choices([1, 2.5, 5, 7.5, 12], weights=[
                                         100, 80, 75, 70, 60], k=1)[0]

    def get_hp(self):
        return self.hp

    def get_atk_power(self):
        return self.atk_power

    def get_defence_str(self):
        return self.defence_str

    def do_defend(self):
        block = int(self.defence_str // 7)
        return block

    def do_heal(self):
        possible_heals = [250, 500, 750, 1000, 2000, 7000]
        heal_amt = random.choices(possible_heals, weights=[
                                  60, 50, 40, 30, 20, 18], k=1)[0]
        return heal_amt

    def show_stats(self):
        print(f"{self.__class__.__name__} - {self.name}")
        print(f"Health: {self.hp}")
        print(f"ATK: {self.atk_power}")
        print(f"DEF: {self.defence_str}")


# Shield/Tank
class Tank(Character):
    def __init__(self, name):
        super().__init__(name)

        self.hp = int(self.hp * 2)
        self.atk_power = int((self.atk_power * self.crt_chance) * 0.75)
        self.defence_str = int(self.defence_str * 5)


# Main DPS
class Swordsman(Character):
    def __init__(self, name):
        super().__init__(name)

        self.hp = int(self.hp * 0.75)
        self.atk_power = int(self.atk_power * 2)
        self.defence_str = int(self.defence_str * 0.75)


# Buffer
class Wizard(Character):
    def __init__(self, name):
        super().__init__(name)

        self.atk_power = int(self.atk_power * 1.25)


# Healer
class Elf(Character):
    def __init__(self, name):
        super().__init__(name)

        self.hp = int(self.hp * 1.25)
        self.defence_str = int(self.defence_str * 0.5)


# Enemy
class Dragon(Character):
    def __init__(self, name):
        super().__init__(name)

        self.hp = int(self.hp * 5)
        self.atk_power = int(self.atk_power * 5)
        self.defence_str = int(self.defence_str * 3)


# tank = Tank("Sir Tanksalot")
# swordsman = Swordsman("Stabby McStabface")
# wizard = Wizard("Spellbert Einstein")
# elf = Elf("Florence NightingElf")
# dragon = Dragon("Draggin Yaface")
