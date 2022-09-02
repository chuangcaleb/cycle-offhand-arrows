scoreboard players add @s cc.ca.pointer 1
execute if score @s cc.ca.initial = @s cc.ca.pointer run item replace entity @s weapon.offhand from entity @e[tag=cc.ca.temp_item,limit=1] weapon
execute unless score @s cc.ca.initial = @s cc.ca.pointer run function cchesed:cyofar/check_slot/1