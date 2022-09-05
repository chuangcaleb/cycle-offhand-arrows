# ----------------------------------- Tick ----------------------------------- #

# Tag all players with bow in mainhand and arrows in offhand
execute as @a[tag=!cc.ca.standby] if predicate cchesed:cyofar/standby run tag @s add cc.ca.standby
# Process all tagged players
execute as @a[tag=cc.ca.standby] run function cchesed:cyofar/tick_standby
