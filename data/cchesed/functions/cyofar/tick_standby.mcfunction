 # ---------------------------------------------------------------------------- #
 #            Process all tagged players who have swapped those items           #
 # ---------------------------------------------------------------------------- 

# If swapped hands, then attempt to cycle through arrows
execute if predicate cchesed:cyofar/active run function cchesed:cyofar/cycle
# Otherwise, untag all players who are not on standby anymore
execute unless predicate cchesed:cyofar/standby run tag @s remove cc.ca.standby


