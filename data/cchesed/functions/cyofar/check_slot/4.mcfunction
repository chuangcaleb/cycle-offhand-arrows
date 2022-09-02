execute if data entity @s Inventory[{Slot:4b,id:"minecraft:arrow"}] run data modify storage cchesed:cyofar ArrowSlot set value 1b
execute if data entity @s Inventory[{Slot:4b,id:"minecraft:tipped_arrow"}] run data modify storage cchesed:cyofar ArrowSlot set value 1b
execute if data entity @s Inventory[{Slot:4b,id:"minecraft:firework_rocket"}] run data modify storage cchesed:cyofar ArrowSlot set value 1b
execute if data storage cchesed:cyofar {ArrowSlot:1b} run say WOW
execute if data storage cchesed:cyofar {ArrowSlot:0b} run say nope