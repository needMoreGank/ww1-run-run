tiles.set_current_tilemap(tilemap("""level1"""))
# tile size is 1enum)s FOR REAL TO SEE IF IT WORKS
# GITHUB AGAINST
#enum = 
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
    rightBullet.set_position(270, randint(16, 496))
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
landmine = sprites.create(img("""
    . . . . 6 6 6 6 6 6 6 . . . . .
    . . 6 6 6 6 6 6 6 6 6 6 6 . . .
    . 6 6 6 6 6 6 6 6 6 6 6 6 6 . .
    . 6 6 6 6 6 6 6 6 6 6 6 6 6 . .
    6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 .
    6 6 6 6 6 6 6 f 6 6 2 6 6 6 6 .
    6 6 6 6 6 6 f f f 6 6 6 6 6 6 .
    6 6 6 6 6 f f f f f 6 6 6 6 6 .
    6 6 6 6 6 6 f f f 6 6 6 6 6 6 .
    6 6 6 6 6 6 6 f 6 6 6 6 6 6 6 .
    6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 .
    . 6 6 6 6 6 6 6 6 6 6 6 6 6 . .
    . 6 6 6 6 6 6 6 6 6 6 6 6 6 . .
    . . 6 6 6 6 6 6 6 6 6 6 6 . . .
    . . . . 6 6 6 6 6 6 6 . . . . .
    . . . . . . . . . . . . . . . .
"""),
    SpriteKind.enemy)