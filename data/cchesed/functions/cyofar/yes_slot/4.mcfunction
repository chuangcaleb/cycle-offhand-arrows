say yes 4
scoreboard players set @s cc.ca.current 0
item replace entity @s weapon.offhand from entity @s container.4
item replace entity @s container.4 from entity @e[tag=cc.ca.temp_item,limit=1] weapon
data modify storage cchesed:cyofar HasSwapped set value 1b