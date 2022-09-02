say not 0
scoreboard players add @s cc.ca.current 1
execute if score @s cc.ca.initial = @s cc.ca.current run item replace entity @s weapon.offhand from entity @e[tag=cc.ca.temp_item,limit=1] weapon
execute unless score @s cc.ca.initial = @s cc.ca.current run function cchesed:cyofar/check_slot/1