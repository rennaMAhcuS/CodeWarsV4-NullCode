# Components
1. [Map](#map)
2. [Team](#team)
3. [Resources](#resources)
4. [Base](#base)
5. [Robots](#robots)


## Map

The Map is a randomly generated square grid of tiles (typically `40 x 40`), that contain 3 islands of size `3 x 3`, and collectible resources scattered across most of the remaining tiles.

The islands are spawned such that on symmetrically dividing the map into 4 quadrants, 3 of them have islands. The two opposite corners of the map in quadrants with islands are chosen, and set as the deploy points for each team's pirates (the location where new pirates are spawned). 

![A screenshot of the Map mid-game](./media/screenshot.jpg)
> _A screenshot of the Map mid-game, with lines drawn to show the 4 quadrants_

Whenever a pirate (or pirates) land on a tile with a resource, it gets distributed between both teams depending on the proportion of pirates present at that spot, and the resource is exhausted.

Most of these resources are not replenished (see [Resources](#resources)).

## Team

There are two teams in the game: **Red** and **Blue**

At the start of the team, both of the two teams are provided with `X` Rum, `X` Wood and `X` Gunpowder. Each team is also assigned one deploy point (see [Map](#map)).



## Resources

There are 3 resources that you will find scattered the map. Resources are collected by a team when their pirates move onto tiles that contain them. These resources are **shared commonly by the whole team**, and play different roles in the game:

### Rum
Rum is used to spawn more pirates at the team's deploy point. It is used automatically at collection, and each pirate costs `50` Rum. 

Rum is never replenished, and is thus a limited resource on the Map.

### Wood
Wood is used to build walls around islands the team is occupying. Building walls costs `50` Wood, and the team must decide when to use this resource. 

Wood is never replenished, and is thus a limited resource on the Map.

### Gunpowder
Gunpowder is an important resource used in battles, when pirates come in contact with each other <u>i.e.</u> move onto the same tile.

If the pirate's team has atleast `100` Gunpowder, then the pirate destroys the enemy pirate. j

Gunpowder is periodically replenished on the Map if its amount falls below a certain threshold.

## Base

The Base has the power to create robots and providing them with a signal while doing so. Apart from that, every robot could put up a signal of its own, which could only be read and interpreted at its parent base, to decide on future strategy.

It could also deploy virus, if it gets surrounded by enemy bots.

## Pirates

Pirates are the functional units of a team, that explore the map, collect resources and capture islands.

The primary action that a pirate can perform is to **move**, and to decide where to move it can investigate its surroundings and communicate with its team via signals.

Each ship occupies exactly one tile at any time, and any tile that has one or more ships from a team will have a boat displayed on it.

## 2. Communication Between Base and Robots

There are three types of Signals in the game:

1. Those passed onto Robots, when they are created (by the Base Function)
2. Those which are put up by the base and could be read by all of its robots
3. Those which are put up by robots and can be read by the parent base

These could be used to co-ordinate movements and strategise attacks/defence.