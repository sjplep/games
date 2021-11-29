<h2>Hunt the Wumpus</h2>
<h5><i>An interactive fiction text adventure written in Ink.<i></h5>

// add an image here
// https://sjplep.itch.io/wumpus-interactive-fiction-game
// * an event happens once
// + an event happens multiple times eg visiting the same room
// === a knot
// { conditional on having visited a location previously - if not, use 'not' otherwise just use {

Your fellow adventurers have been trapped in the castle dungeons by the deadly <b>wumpus.</b> 
Will <i>you</i> dare enter the dungeons to save them?

* [Enter the dungeons]
You enter the Dungeon and attempt to save your friends. How commendable.
-> enter_dungeon
* [Run away]
You have abandoned your quest, leaving your friends to their fate. You are a miserable coward, but at least you live. But is it worth it?

=== enter_dungeon ===
You are at the dungeon entrance, not much more than a hole in the ground. A broad tunnel leads left and right. There is a smaller tunnel leading down.
+ [Go left]
-> left_wing
+ [Go right]
-> right_wing
+ [Go down]
-> lower_level
* [Exit the dungeon]
You have abandoned your quest, leaving your friends to their fate. You are a miserable coward, but at least you live. But is it worth it?
-> END

=== left_wing ===
The walls are damp with the slime and smell of wumpus. The tunnel leads left and right. Or you can turn back.
+ [Go left]
-> room1
+ [Go right]
-> room2
+ [Go back]
-> enter_dungeon

=== left_wing_got_key ===
+ [Go left]
-> room1_got_key
+ [Go right]
-> room2
+ [Go back]
-> enter_dungeon

=== right_wing ===
You are at an intersection. A gentle breeze blows from the left. You can go left or right, or you can turn back.
+ [Go left]
-> room3
+ [Go right]
-> room4
+ [Go back]
-> enter_dungeon

=== lower_level ===
You are in the lower levels. A corridor goes left and right, or you can climb back up.
+ [Go left]
-> room5
+ [Go right]
-> room6
+ [Climb up]
-> enter_dungeon

=== room1 ===
You are at a dead end. 
There is a golden key here.
+ [Go back]
-> left_wing
+ [Get key]
You get the key.
-> room1_got_key

=== room1_got_key ===
You are at a dead end.
+ [Go back]
-> left_wing_got_key

=== room2 ===
Startled, you spot the deadly wumpus and it looks hungry! Before you can react, it bites your head off! Your quest, and your life, is over!
-> END

=== room3 ===
You fall down a pit. You are helplessly trapped and will make a tasty meal for the wumpus, when it comes round sooner or later. Your quest is over.
-> END

=== room4 ===
{not room1_got_key: You find a sealed door behind which you hear the terrified cries of your friends. The door is too sturdy to kick down. You spy a keyhole... if only you had a key... Suddenly your torch flickers and is extinguished, leaving you trapped in the dark. You try to stumble out the way you came but you are helplessly lost and a mark for the wumpus. Your quest ends here, and so do you.}
{room1_got_key: You find a sealed door behind which you hear the terrified cries of your friends. The door is too sturdy to kick down. You spy a keyhole and place the key you found earlier in it... it turns! The door opens and lead your grateful friends back out of the dungeons! Congratulations on completing your quest.}
-> END

=== room5 ===
A cloud of bats suddenly appears out of nowhere, lifts you up and drops you somewhere else in this maze of a dungeon!
-> left_wing

=== room6 ===
You are at a dead end.
There is a red herring here.
+ [Go back]
-> lower_level
+ [Get herring]
-> get_herring

=== get_herring ===
You try to get the red herring but it slips out of your hand!
+ [Go back]
-> lower_level
+ [Try again]
-> get_herring





