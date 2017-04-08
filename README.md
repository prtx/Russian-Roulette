# Russian Roulette

**DISCLAIMER: THIS PROGRAM IS INTENDED TO DELETE ALL FILES FROM THE SYSTEM. IN NO EVENT SHALL THE
AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY ARISING FROM, OUT OF OR IN CONNECTION WITH THE PROGRAM.**

[Russian roulette](https://en.wikipedia.org/wiki/Russian_roulette) is a lethal game of chance in which a player places a single round in a revolver, spins the cylinder, places the muzzle against their head, and pulls the trigger. This program imitates the game via command line. If you lose, sudo rm/* is executed on your machine.

## Get it
```
$ git clone https://github.com/prtx/Russian-Roulette
```

## How to Play

**Via Host**
```
$ sudo python3 roulette.py --host
```

**Via Client**
```
$ sudo python3 roulette.py --connect [ip]
```

**Bypass sudo rm/***
```
$ sudo python3 roulette.py --host --pussy-mode
```