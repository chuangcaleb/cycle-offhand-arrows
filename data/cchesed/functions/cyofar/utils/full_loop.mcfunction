# Put back the offhand arrow
item replace entity @s weapon.offhand from entity @e[tag=cc.ca.temp_item,limit=1] weapon
# Play sound
stopsound @a[distance=..16] player item.crossbow.loading_end
playsound item.crossbow.loading_end player @a[distance=..16] ~ ~ ~ 1 2