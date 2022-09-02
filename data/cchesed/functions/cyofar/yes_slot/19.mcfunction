scoreboard players add @s cc.ca.pointer 1
item replace entity @s weapon.offhand from entity @s container.19
item replace entity @s container.19 from entity @e[tag=cc.ca.temp_item,limit=1] weapon
data modify storage cchesed:cyofar HasSwapped set value 1b
function cchesed:cyofar/utils/swap_sound