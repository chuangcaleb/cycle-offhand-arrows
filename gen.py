from string import Template
from pprint import pprint


def list_to_str(list):
    return "\n".join(list)


inv_limit = 5

base_path = "data/cchesed/functions/cyofar/"

ammo_list = ["arrow", "spectral_arrow", "tipped_arrow", "firework_rocket"]

check_t = Template(
    'execute if data entity @s Inventory[{Slot:${count}b,id:"minecraft:${ammo}"}] run data modify storage cchesed:cyofar IsArrowSlot set value 1b'
)

check_all_list = []

for count in range(0, inv_limit):

    # Get next index, loops around/overflows if at max/endc
    not_limit = True if count < inv_limit - 1 else False
    next_i = count + 1 if count < inv_limit - 1 else 0

    # Check
    check_list = [
        f"say check {count}",
        "data modify storage cchesed:cyofar IsArrowSlot set value 0b"
    ]
    check_list.extend([
        check_t.substitute(ammo=ammo, count=count)
        for ammo in ammo_list
    ])
    check_list.extend([
        f"execute if data storage cchesed:cyofar {{IsArrowSlot:1b}} run function cchesed:cyofar/yes_slot/{count}",
        f"execute if data storage cchesed:cyofar {{IsArrowSlot:0b}} run function cchesed:cyofar/not_slot/{count}"
    ])

    with open(base_path + "check_slot/" + str(count) + ".mcfunction", 'w') as file:
        file.writelines(list_to_str(check_list))

    # Case: not arrow
    not_list = [
        f"say not {count}",
        "scoreboard players add @s cc.ca.current 1" if not_limit else "scoreboard players set @s cc.ca.current 0",  # Increment pointer
        # If looped back, then just switch back
        # "execute if score @s cc.ca.initial = @s cc.ca.current run say switch",
        "execute if score @s cc.ca.initial = @s cc.ca.current run item replace entity @s weapon.offhand from entity @e[tag=cc.ca.temp_item,limit=1] weapon",
        f"execute unless score @s cc.ca.initial = @s cc.ca.current run function cchesed:cyofar/check_slot/{next_i}"
    ]
    with open(base_path + "not_slot/" + str(count) + ".mcfunction", 'w') as file:
        file.writelines(list_to_str(not_list))

    # Case: yes arrow
    yes_list = [
        f"say yes {count}",
        "scoreboard players add @s cc.ca.current 1" if not_limit else "scoreboard players set @s cc.ca.current 0",  # Increment pointer
        f"item replace entity @s weapon.offhand from entity @s container.{count}",
        f"item replace entity @s container.{count} from entity @e[tag=cc.ca.temp_item,limit=1] weapon",
        "data modify storage cchesed:cyofar HasSwapped set value 1b"
    ]
    with open(base_path + "yes_slot/" + str(count) + ".mcfunction", 'w') as file:
        file.writelines(list_to_str(yes_list))

    # Check All
    all_str = "execute if score @s cc.ca.current matches ${count} if data storage cchesed:cyofar {HasSwapped:0b} run function cchesed:cyofar/check_slot/${count}"
    t_all = Template(all_str)
    check_all_str = t_all.substitute(count=count)
    check_all_list.append(check_all_str)


with open(base_path + "check_slot/check_all.mcfunction", 'w') as file:
    file.writelines(list_to_str(check_all_list))
