# Cycle Offhand Arrows

> Cycle through arrow types in the offhand slot by using your offhand key whilst holding a Bow or Crossbow!

https://user-images.githubusercontent.com/62867911/188391208-dd7e4895-39ce-403a-8a7c-0f29d9e46aeb.mov

## Motivation

There's a bunch of interesting arrows you can shoot in the game. Arrows, Spectral Arrows, Firework Rockets, and a wide arsenal of Tipped Arrows. But how often in practice do you actually carry and use more than one type of arrow?

**It's a hassle to pack many types of arrows.** Usually you'd stow them all away in your inventory somewhere, keeping your hotbar for more important items. You simply shoot from your bow or crossbow, not knowing which arrow gets shot out.

In the end, nobody even bothers to use anything other than the regular Arrow, or perhaps even the Spectral Arrow since they're both farmable. And that's a shame, because there's so many interesting applications to all the Tipped Arrows!

## Design

> **tl;dr, hold a (cross)bow in your mainhand and have arrows in your offhand, and press your (Swap) Offhand hotkey to cycle through arrows from your inventory, within the offhand slot.**

The solution to this was to create a system to help players use different arrows easily. I wanted something that was elegant and user-friendly.

By selecting a Bow or Crossbow in the mainhand whilst a (Spectral/Tipped) Arrow or Firework Rocket is in the offhand, a player can trigger the system with the (Swap) Offhand hotkey. Usually this would swap the bow into the offhand and arrow into the mainhand.

Instead, the (Cross)Bow will stay in the mainhand whilst the arrow(s) in the offhand slot will get swapped with the next arrow slot in the inventory, and the next one, and so on.

It's quite simple.

The idea is that the projectile in the offhand slot will have top priority amd will always be used when you use a (cross)bow. This is a useful benefit, because **you can see your currently selected arrow in your offhand slot from your HUD**. All without opening the clunky inventory GUI.

## Limitations

For a basic and simple system, there's really not much to ask for! It works flawlessly for what it is.

One small attribute is that the system simply cycles through any inventory slot with the right item (arrows + rockets). This means that it does not group stacks of the same item together, and will treat them as separate items: for example, 3 stacks of regular Arrows have to be cycled through three separate times. I left it at this because to group items, Tipped Arrows and Firework Rockets have complex NBT, and there's no easy way to group every case.

Additionally, when the the projectiles in the offhand slot are depleted (e.g. you use up your last Arrow), then your offhand will be empty; using the offhand key now will simply move your (cross)bow into the offhand. You'd have to manually put back whatever projectile into the offhand slot. I didn't want to make an auto-refill system.
