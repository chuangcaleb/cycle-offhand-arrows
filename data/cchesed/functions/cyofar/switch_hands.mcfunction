summon armor_stand ~ -300 ~ {Tags:["cc.ca.temp_item"],HandItems:[{id:"minecraft:air",Count:1b},{}]}
data modify entity @e[tag=cc.ca.temp_item,limit=1] HandItems[0] set from entity @s SelectedItem
item replace entity @s weapon.mainhand from entity @s weapon.offhand
item replace entity @s weapon.offhand from entity @e[tag=cc.ca.temp_item,limit=1] weapon