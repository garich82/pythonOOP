from typing import Dict


class Player:
    def __init__(self, name: str, hp: int, mp:int):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.skills = Dict[str: int] = {}
        self.guild = "Unaffiliated"

    def add_skill(self, skill_name, mana_cost):
        if skill_name in self.skills:
            return "Skill already added"
        self.skills[skill_name] = mana_cost
        return f"Skill {skill_name} added to the collection of the player {self.name}"

    def player_info(self):
        info = f"Name: {self.name}\nGuild: {self.guild}\nHP: {self.hp}\nMP: {self.mp}\n"
        info += "\n".join([f"==={skill} - {mana}" for skill, mana in self.skills.items()])
        return info


