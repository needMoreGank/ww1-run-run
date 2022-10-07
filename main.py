tiles.set_current_tilemap(tilemap("""level1"""))
#tile size = 16
#10x160 = 160 X 144
#16x32 = 512 Y 496
scene.set_background_image(img("""
    ................................................................................................................................................................
    ................................................................................................................................................................
    ................................................................................................................................................................
    ................................................................................................................................................................
    ................................................................................................................................................................
    ................................................................................................................................................................
    ................................................................................................................................................................
    ................................................................................................................................................................
    ................................................................................................................................................................
    ................................................................................................................................................................
    ................................................................................................................................................................
    ................................................................................................................................................................
    ................................................................................................................................................................
    ................................................................................................................................................................
    ................................................................................................................................................................
    ................................................................................................................................................................
    ................................................................................................................................................................
    ................................................................................................................................................................
    ................................................................................................................................................................
    ................................................................................................................................................................
    ............................fffffffffffffffffffff...............................................................................................................
    ..........................fffffffffffffffffffffffff.............................................................................................................
    ........................ffffffffffffffffffffffffffff............................................................................................................
    ......................ffffffff.................ffffff...........................................................................................................
    .....................fffffff.....................fffff..........................................................................................................
    ....................ffffff........................ffff...............................................................ffffffff...................................
    ...................fffff...........................ffff.........................................................fffffffffffffff.................................
    ..................fffff............................fffff......................................................fffffffffffffffffff...............................
    .................fffff..............................fffff....................................................ffffffffff....ffffffff.............................
    .................ffff....ffff........................fffff..................................................ffffff...........fffffff............................
    ................ffff.....ffff.............fff.........fffff................................................fffff...............fffff............................
    ...............fffff.....fffff...........ffff..........ffff................................................ffff..................ffff...........................
    ...............ffff.......fffff........ffffff...........fff...............................................ffff...................fffff..........................
    ...............fff.........ffffff....fffffff............fff..............................................fffff....................fffff.........................
    ...............ffff.........ffffff.ffffffff.............fff..............................................ffff......................ffff.........................
    ...............ffff..........ffffffffffff...............fff..............................................fff........................fff.........................
    ................fff............ffffffff.................ffff............................................ffff........................ffff........................
    ................fff.............fffff...................ffff............................................ffff........................ffff........................
    ................fff......................................fff............................................fff.....fff..fff.............fff........................
    ................fff......................................fff...........................................ffff.....ffffffff.............ffff.......................
    ................fff........fff.......fff.................fff...........................................ffff.....ffffffff....ffff.....ffff.......................
    ................fff........fff.......fff.................fff...........................................fff.......ffffff.....ffff.ffff.fff.......................
    ................fff........fff.......fff.................fff...........................................fff.......fffffff....fffffffff.fff.......................
    ................fff......................................fff........................................bbbbbbb......fffffff.....ffffffff.fff.......................
    ................fff......................fff.............fff........................................bbbbbbb......fff.fff.....fffffff..fff.......................
    ................fff.....................ffff............ffff........................................bbbbbbb..................fffffff..fff.......................
    ................fff.........fff.......ffffff............ffff...........................................fff...................fffffff..fff.......................
    ................ffff........fffffffffffffff............ffff............................................ffff..................fff......fff.......................
    ................fffff.......ffffffffffffff.............ffff............................................fffff..........................fff.......................
    .................fffff.......fffffffffff..............ffff..fffffffffffffffffffffffffffff...............fffff.........................fff.......................
    ..................ffff................................ffff..fffffffffffffffffffffffffffff................ffff......fffff.............ffff.......................
    ...................ffff..............................ffff..ffffffffffffffffffffffffffffff.................ffff.....ffffffff..........ffff.......................
    ...................fffff............................fffff..ffff.......................fff.................fffff....ffffffffff........fff........................
    ....................fffff..........................fffff...fff........................fff..................fffff......fffffff........fff........................
    .....................fffff........................fffff....fff.................ffffffffff...................fffff........ffff.......ffff........................
    ......................ffff.......................fffff.....fff.......ffffffffffffffffffff....................ffff...................ffff........................
    .......................ffffff...............fffffffff......fff.....ffffffffffffffffffffff.....................fffff................ffff.........................
    .......................ffffffffff.ffffffffffffffffff.......fff.....ffffffffffffff.............................fffffff............ffffff.........................
    ........................fffffffffffffffffffffffffff........fff....fffff.ffff...................................fffffffff.....fffffffff..........................
    ...........................fffffffffffffffffff.............ffff...ffffffffff............................fff......ffffffffffffffffffff...........................
    ...............................ffffffff....................ffff...fffffffff.............................ffff.......ffffffffffffffff.............................
    ....................................fff....................ffffffffffffffff.............................fffff.........fffffffff.................................
    ....................................fff....................ffffffffff....................................fffff...........fff....................................
    ....................................fff....................ffffffffff.....................................fffff..........fff....................................
    ....................................fff....................ffff.fffff......................................fffff........ffff....................................
    ....................................fff...................ffff..............................................fffff.......ffff....................................
    ....................................fff...................ffff...............................................fffff......fff.....................................
    ....................................fff...................fff.................................................fffff....ffff.....................................
    ....................................fff..................ffff..................................................fffff...ffff.....................................
    ....................................fff..................ffff...................................................fffff..fff......................................
    ....................................fffffffffff..........fff.....................................................ffff.ffff......................................
    ....................................ffffffffffff.........fff......................................................ffffffff......................................
    ....................................fffffffffffff.......ffff......................................................ffffffffffffffffff............................
    ....................................fff......fffff......ffff.......................................................fffffffffffffffffffffffffffff................
    ....................................fff.......fffff.....fff.........................................................fffffffffffffffffffffffffffffffffff.........
    ....................................fff........fffff....fff..........................................................ffff.........ffffffffffffffffffffffff......
    ....................................fff.........fffff..ffff.........................................................ffff......................ffffffffffff......
    ....................................fff..........fffff.ffff.........................................................ffff.............................fffff......
    ....................................fff...........ffffffff..........................................................fff.........................................
    ....................................fff............fffffff.........................................................ffff.........................................
    ....................................fff.............fffff..........................................................ffff.........................................
    ....................................fff..............ffff..........................................................fff..........................................
    ....................................fff...........................................................................ffff..........................................
    ....................................fff...........................................................................ffff..........................................
    ....................................fff...........................................................................fff...........................................
    ....................................fff..........................................................................ffff...........................................
    ....................................fff..........................................................................ffff...........................................
    ....................................fff.........................................................................ffff............................................
    ....................................fff.........................................................................ffff............................................
    ....................................fff......................................................................ffffff.............................................
    ....................................fff.....................................................................fffffff.............................................
    ....................................fff...................................................................fffffffff.............................................
    ....................................fff..................................................................ffffff.fff.............................................
    ....................................fffff..............................................................fffffff..fff.............................................
    ....................................ffffff...........................................................fffffff....ffff............................................
    ....................................ffffff.......................................................ffffffffff.....ffff............................................
    ....................................fffffff..................................................ffffffffffff........fff............................................
    ...................................fffffffff...............................................ffffffffffff..........fff............................................
    ...................................ffff.ffff...............................................ffffffff..............fff............................................
    ..................................ffff...fff...............................................ffff..................ffff...........................................
    .................................fffff...ffff....................................................................ffff...........................................
    ................................fffff....ffff.....................................................................fff...........................................
    ................................ffff......ffff....................................................................fff...........................................
    ...............................ffff.......ffff....................................................................fff...........................................
    ..............................fffff........fff....................................................................fff...........................................
    .............................fffff.........ffff...................................................................fff...........................................
    ............................fffff..........ffff...................................................................ffff..........................................
    ............................ffff............ffff..................................................................ffff..........................................
    ...........................ffff.............ffff...................................................................fff..........................................
    ..........................fffff..............fff...................................................................fff..........................................
    .........................fffff...............fff...................................................................fff..........................................
    .........................ffff................fff...................................................................fff..........................................
    ........................ffff.................fff................................................................................................................
    .......................fffff.................ffff...............................................................................................................
    .......................ffff..................ffff...............................................................................................................
    .......................fff....................fff...............................................................................................................
    .....................fff......................fff...............................................................................................................
    .....................fff......................fff...............................................................................................................
    ....................ffff......................ffff..............................................................................................................
    ....................ffff......................ffff..............................................................................................................
"""))

hp_max = 100
hp = hp_max
messenger = sprites.create(img("""
        . . . . . . f f f f . . . . . . 
            . . . . f f f 2 2 f f f . . . . 
            . . . f f f 2 2 2 2 f f f . . . 
            . . f f f e e e e e e f f f . . 
            . . f f e 2 2 2 2 2 2 e e f . . 
            . . f e 2 f f f f f f 2 e f . . 
            . . f f f f e e e e f f f f . . 
            . f f e f b f 4 4 f b f e f f . 
            . f e e 4 1 f d d f 1 4 e e f . 
            . . f e e d d d d d d e e f . . 
            . . . f e e 4 4 4 4 e e f . . . 
            . . e 4 f 2 2 2 2 2 2 f 4 e . . 
            . . 4 d f 2 2 2 2 2 2 f d 4 . . 
            . . 4 4 f 4 4 5 5 4 4 f 4 4 . . 
            . . . . . f f f f f f . . . . . 
            . . . . . f f . . f f . . . . .
    """),
    SpriteKind.player)
currentScene = "game"
controller.move_sprite(messenger)
scene.camera_follow_sprite(messenger)
messenger.setPosition()


def spawn_leftBullet():
    leftBullet = sprites.create(img("""
        . . . . . . . .
        . . . . . . . .
        . . . . . . . .
        . 5 f 5 5 5 . .
        . 5 f 5 5 5 5 .
        . 5 f 5 5 5 . .
        . . . . . . . .
        . . . . . . . .
    """), SpriteKind.projectile)
    leftBullet.set_position(0, randint(16, 496))
    leftBullet.set_velocity(randint(60, 130), 0)
    leftBullet.start_effect(effects.trail)
game.on_update_interval(randint(500, 1000), spawn_leftBullet)

def spawn_rightBullet():
    rightBullet = sprites.create(img("""
        . . . . . . . .
        . . . . . . . .
        . . . . . . . .
        . . 5 5 5 f 5 .
        . 5 5 5 5 f 5 .
        . . 5 5 5 f 5 .
        . . . . . . . .
        . . . . . . . .
    """), SpriteKind.projectile)
    rightBullet.set_position(160, randint(16, 496))
    rightBullet.set_velocity(randint(-60, -130), 0)
    rightBullet.start_effect(effects.trail)
    
game.on_update_interval(randint(500, 1000), spawn_rightBullet)

def on_hit_wall(sprite, location):
    sprite.destroy()
scene.on_hit_wall(SpriteKind.projectile, on_hit_wall)
def hit_bullet(sprite, bullet):
    global hp
    hp = hp - 20
    if hp == 0:
        game.over(False)
    bullet.destroy()

sprites.on_overlap(SpriteKind.player, SpriteKind.projectile, hit_bullet)

#barbed_wire
wire = sprites.create(img("""
    f f f f 1 f f f f 1 f f f f f f
    f f f f 1 f f f f 1 f f 1 f f f
    f f f f 1 f f f 1 f f f 1 f f f
    f f f f 1 f f f 1 f f f 1 f f f
    f f 1 1 f f f 1 1 f f 1 f f f f
    f 1 f f f f f 1 f f f 1 f f f f
    f f f f f f f f f f f 1 f f f f
    f f f f f f f f f f f f f f f f
"""),
    SpriteKind.enemy)


wire.set_position(30, 30)
scaling.scale_to_pixels(wire, randint(32, 64), ScaleDirection.HORIZONTALLY, ScaleAnchor.MIDDLE)

#landmine

def spawn_landmine():
    landmine = sprites.create(img("""
        . . . . . . . . . . . .
        . . . 6 6 6 6 6 6 . . .
        . . 6 6 6 6 6 6 6 6 . .
        . 6 6 6 6 6 6 6 6 6 6 .
        . 6 6 6 6 6 6 2 6 6 6 .
        . 6 6 6 6 f f 6 6 6 6 .
        . 6 6 6 f f f f 6 6 6 .
        . 6 6 6 6 f f 6 6 6 6 .
        . 6 6 6 6 6 6 6 6 6 6 .
        . . 6 6 6 6 6 6 6 6 . .
        . . . 6 6 6 6 6 6 . . .
        . . . . . . . . . . . .
    """),
        SpriteKind.enemy)
    landmine.set_position(randint(16, 144), randint(16, 496))

for x in range(randint(6, 11)):
    spawn_landmine()