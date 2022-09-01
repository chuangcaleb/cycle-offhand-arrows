from string import Template
from pprint import pprint


def list_to_str(list):
    return "\n".join(list)


base_path = "data/cchesed/functions/cyofar/"

ammo_list = ["arrow", "tipped_arrow", "firework_rocket"]

check_str = 'execute if data entity @s Inventory[{Slot:${count}b,id:"minecraft:${ammo}"}] run say Arrow in ${count}!'


t = Template(check_str)

check_all_list = []

for count in range(0, 5):

    str_list = [
        t.substitute(ammo=ammo, count=count)
        for ammo in ammo_list
    ]

    # pprint(str_list)

    with open(base_path + "check_slot/" + str(count) + ".mcfunction", 'w') as file:
        file.writelines(list_to_str(str_list))
    
	# Check All
    all_str = "execute if score @s cc.ca.current matches ${count} run function cchesed:cyofar/check_slot/${count}"
    t_all = Template(all_str)
    check_all_str = t_all.substitute(count=count)
    check_all_list.append(check_all_str)


with open(base_path + "check_slot/check_all.mcfunction", 'w') as file:
    file.writelines(list_to_str(check_all_list))
