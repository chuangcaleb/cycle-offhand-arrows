# Initialize score if not initalized already
execute unless score @s cc.ca.current matches 0.. run scoreboard players set @s cc.ca.current 0

data modify storage cchesed:cyofar ArrowSlot set value 0b
function cchesed:cyofar/check_slot/check_all