say not 4
scoreboard players set @s cc.ca.current 0
execute if score @s cc.ca.initial = @s cc.ca.current run item replace entity @s weapon.offhand from entity @e[tag=cc.ca.temp_item,limit=1] weapon
execute unless score @s cc.ca.initial = @s cc.ca.current run function cchesed:cyofar/check_slot/0