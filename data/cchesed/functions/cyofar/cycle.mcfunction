# Initialize score if not initalized already
execute unless score @s cc.ca.current matches 0.. run scoreboard players set @s cc.ca.current 0

# Store initial slot to check if we've made a full loop pass through the inv
# execute store result storage cchesed:cyofar IntialSlot int 1 run scoreboard players get @s cc.ca.current
scoreboard players operation @s cc.ca.initial = @s cc.ca.current
say cycle

# HB: Switch bow back into hotbar, save arrow in armor stand
summon armor_stand ~ -300 ~ {Tags:["cc.ca.temp_item"],HandItems:[{id:"minecraft:air",Count:1b},{}]}
data modify entity @e[tag=cc.ca.temp_item,limit=1] HandItems[0] set from entity @s SelectedItem
item replace entity @s weapon.mainhand from entity @s weapon.offhand


# Reset the ArrowSlot flag to 0b
# data modify storage cchesed:cyofar IsArrowSlot set value 0b

# Check all slots
function cchesed:cyofar/check_slot/check_all