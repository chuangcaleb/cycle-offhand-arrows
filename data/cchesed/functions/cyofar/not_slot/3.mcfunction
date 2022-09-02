scoreboard players add @s cc.ca.pointer 1
execute if score @s cc.ca.initial = @s cc.ca.pointer run function cchesed:cyofar/utils/full_loop
execute unless score @s cc.ca.initial = @s cc.ca.pointer run function cchesed:cyofar/check_slot/4