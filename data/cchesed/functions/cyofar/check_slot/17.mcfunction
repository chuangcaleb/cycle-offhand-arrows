data modify storage cchesed:cyofar IsArrowSlot set value 0b
execute if data entity @s Inventory[{Slot:17b,id:"minecraft:arrow"}] run data modify storage cchesed:cyofar IsArrowSlot set value 1b
execute if data entity @s Inventory[{Slot:17b,id:"minecraft:spectral_arrow"}] run data modify storage cchesed:cyofar IsArrowSlot set value 1b
execute if data entity @s Inventory[{Slot:17b,id:"minecraft:tipped_arrow"}] run data modify storage cchesed:cyofar IsArrowSlot set value 1b
execute if data entity @s Inventory[{Slot:17b,id:"minecraft:firework_rocket"}] run data modify storage cchesed:cyofar IsArrowSlot set value 1b
execute if data storage cchesed:cyofar {IsArrowSlot:1b} run function cchesed:cyofar/yes_slot/17
execute if data storage cchesed:cyofar {IsArrowSlot:0b} run function cchesed:cyofar/not_slot/17