say yes 0
scoreboard players add @s cc.ca.current 1
item replace entity @s weapon.offhand from entity @s container.0
item replace entity @s container.0 from entity @e[tag=cc.ca.temp_item,limit=1] weapon
data modify storage cchesed:cyofar HasSwapped set value 1b