item replace entity @s weapon.offhand from entity @s container.17
item replace entity @s container.17 from entity @e[tag=cc.ca.temp_item,limit=1] weapon
data modify storage cchesed:cyofar HasSwapped set value 1b
execute at @s run function cchesed:cyofar/utils/swap_sound