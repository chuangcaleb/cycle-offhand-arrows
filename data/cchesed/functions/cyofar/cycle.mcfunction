# Initialize score if not initalized already
execute unless score @s cc.ca.current matches 0.. run scoreboard players set @s cc.ca.current 0

# Store initial slot to check if we've made a full loop pass through the inv
execute store result storage cchesed:cyofar IntialSlot int 1 run scoreboard players get @s cc.ca.current
# Reset the ArrowSlot flag to 0b
data modify storage cchesed:cyofar IsArrowSlot set value 0b

# Check all slots
function cchesed:cyofar/check_slot/check_all