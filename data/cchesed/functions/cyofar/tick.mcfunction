# ----------------------------------- Tick ----------------------------------- #

# Tag all players with bow in mainhand and arrows in offhand
execute as @a[predicate=cchesed:cyofar/standby] run tag @s add cc.ca.standby
# Process all tagged players who have swapped those items
execute as @a[tag=cc.ca.standby,predicate=cchesed:cyofar/active] run function cchesed:cyofar/cycle
# Otherwise, untag all players who are not on standby anymore
execute as @a[predicate=!cchesed:cyofar/standby] run tag @s remove cc.ca.standby

