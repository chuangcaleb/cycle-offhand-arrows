from string import Template
from pprint import pprint
import json 

def list_to_str(list):
    return "\n".join(list)


# with open('ammo_slots_template.json') as f:
    # pred_temp_json = json.loads(f)
# pred_temp_json = json.load(open('ammo_slots_template.json', 'r'))
# print(pred_temp_json)

# pred_temp = Template(str(pred_temp_json))

inv_limit = 36

base_dir = "data/cchesed/functions/cyofar/"
# pred_dir = "data/cchesed/predicates/cyofar/ammo_slots/"

ammo_list = ["arrow", "spectral_arrow", "tipped_arrow", "firework_rocket"]

check_t = Template(
    'execute if data entity @s Inventory[{Slot:${count}b,id:"minecraft:${ammo}"}] run data modify storage cchesed:cyofar IsArrowSlot set value 1b'
)

check_all_list = []

for count in range(0, inv_limit):

    # Get next index, loops around/overflows if at max/endc
    not_limit = True if count < inv_limit - 1 else False
    next_i = count + 1 if not_limit else 0

    # Check
    check_list = [
        "scoreboard players add @s cc.ca.pointer 1" if not_limit else "scoreboard players set @s cc.ca.pointer 0",  # Increment pointer
        "data modify storage cchesed:cyofar IsArrowSlot set value 0b",
        # f"execute if predicate cchesed:cyofar/ammo_slots/{count} run data modify storage cchesed:cyofar IsArrowSlot set value 1b"
    ]
    check_list.extend([
        check_t.substitute(ammo=ammo, count=count)
        for ammo in ammo_list
    ])
    check_list.extend([
        f"execute if data storage cchesed:cyofar {{IsArrowSlot:1b}} run function cchesed:cyofar/yes_slot/{count}",
        f"execute if data storage cchesed:cyofar {{IsArrowSlot:0b}} run function cchesed:cyofar/not_slot/{count}"
    ])

    with open(f"{base_dir}check_slot/{count}.mcfunction", 'w') as file:
        file.writelines(list_to_str(check_list))

    # Case: not arrow
    not_list = [
        "execute if score @s cc.ca.initial = @s cc.ca.pointer at @s run function cchesed:cyofar/utils/full_loop",
        f"execute unless score @s cc.ca.initial = @s cc.ca.pointer run function cchesed:cyofar/check_slot/{next_i}"
    ]
    with open(f"{base_dir}not_slot/{count}.mcfunction", 'w') as file:
        file.writelines(list_to_str(not_list))

    # Case: yes arrow
    yes_list = [
        f"item replace entity @s weapon.offhand from entity @s container.{count}",
        f"item replace entity @s container.{count} from entity @e[tag=cc.ca.temp_item,limit=1] weapon",
        # 'title @s actionbar {"nbt":"Inventory[{Slot:-106b}]","entity":"@s"}',
        "data modify storage cchesed:cyofar HasSwapped set value 1b",
        "execute at @s run function cchesed:cyofar/utils/swap_sound"
    ]
    with open(f"{base_dir}yes_slot/{count}.mcfunction", 'w') as file:
        file.writelines(list_to_str(yes_list))

    # Check All
    all_str = f"execute if score @s cc.ca.pointer matches {count} if data storage cchesed:cyofar {{HasSwapped:0b}} run function cchesed:cyofar/check_slot/{count}"
    check_all_list.append(all_str)

    # Ammo slot predicate
    # pred_str = pred_temp.substitute(count=count)
    # with open(f"{pred_dir}{count}.json", 'w') as file:
    #     # file.write(pred_dict)
    #     # json.dump(pred_dict,f"{base_dir}{count}.json")
    #     file.write(pred_str)


with open(f"{base_dir}check_slot/check_all.mcfunction", 'w') as file:
    file.writelines(list_to_str(check_all_list))
