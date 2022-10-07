

battleScene = tilemap("""level1""")
introScene = tilemap("""level5""")

currentScene = "Battle"

MineSpriteKind = SpriteKind.create()

def change_Scene(sceneName):
    if sceneName == "Intro":
        tiles.set_current_tilemap(introScene)
        IntroSceneStart()
    else:
        tiles.set_current_tilemap(battleScene)
        BattleSceneStart()
def on_hit_wall(sprite3, location):
        sprite3.destroy()
def on_on_overlap(sprite, mine):
        global hp
        hp = hp - 10
        if hp == 0:
            game.over(False)
        statusbar.value = hp
        mine.destroy()     
def spawn_landmine():
        global landmine
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
            MineSpriteKind)
        landmine.set_position(randint(16, 144), randint(16, 496))
def on_on_overlap2(sprite2, bullet):
    global hp
    hp = hp - 20
    statusbar.value = hp
    if hp == 0:
        game.over(False)
    bullet.destroy()

def on_update_interval():
    global leftBullet
    leftBullet = sprites.create(img("""
                . . . . . . . .
                        . . . . . . . .
                        . . . . . . . .
                        . 5 f 5 5 5 . .
                        . 5 f 5 5 5 5 .
                        . 5 f 5 5 5 . .
                        . . . . . . . .
                        . . . . . . . .
            """),
        SpriteKind.projectile)
    leftBullet.set_position(0, randint(16, 496))
    leftBullet.set_velocity(randint(60, 130), 0)
    leftBullet.start_effect(effects.trail)
def on_update_interval2():
    global rightBullet
    rightBullet = sprites.create(img("""
                    . . . . . . . .
                            . . . . . . . .
                            . . . . . . . .
                            . 5 f 5 5 5 . .
                            . 5 f 5 5 5 5 .
                            . 5 f 5 5 5 . .
                            . . . . . . . .
                            . . . . . . . .
                """),
            SpriteKind.projectile)
    rightBullet.set_position(0, randint(16, 496))
    rightBullet.set_velocity(randint(60, 130), 0)
    rightBullet.start_effect(effects.trail)

rightBullet: Sprite = None
leftBullet: Sprite = None
landmine: Sprite = None
statusbar: StatusBarSprite = None
hp_max = 100
hp = hp_max

def IntroSceneStart():
    my_sprite = sprites.create(img("""
        . . . . . . . . . . b 5 b . . .
        . . . . . . . . . b 5 b . . . .
        . . . . . . . . . b c . . . . .
        . . . . . . b b b b b b . . . .
        . . . . . b b 5 5 5 5 5 b . . .
        . . . . b b 5 d 1 f 5 5 d f . .
        . . . . b 5 5 1 f f 5 d 4 c . .
        . . . . b 5 5 d f b d d 4 4 . .
        b d d d b b d 5 5 5 4 4 4 4 4 b
        b b d 5 5 5 b 5 5 4 4 4 4 4 b .
        b d c 5 5 5 5 d 5 5 5 5 5 b . .
        c d d c d 5 5 b 5 5 5 5 5 5 b .
        c b d d c c b 5 5 5 5 5 5 5 b .
        . c d d d d d d 5 5 5 5 5 d b .
        . . c b d d d d d 5 5 5 b b . .
        . . . c c c c c c c c b b . . .
    """), SpriteKind.player)
def BattleSceneStart():
    global statusbar
    scene.on_hit_wall(SpriteKind.projectile, on_hit_wall)
    sprites.on_overlap(SpriteKind.player, MineSpriteKind, on_on_overlap)
    sprites.on_overlap(SpriteKind.player, SpriteKind.projectile, on_on_overlap2)
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
    controller.move_sprite(messenger)
    scene.camera_follow_sprite(messenger)
    statusbar = statusbars.create(20, 4, StatusBarKind.health)
    statusbar.attach_to_sprite(messenger)
    # barbed_wire
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
    scaling.scale_to_pixels(wire,
        randint(32, 64),
        ScaleDirection.HORIZONTALLY,
        ScaleAnchor.MIDDLE)
    for index in range(randint(6, 11)):
        spawn_landmine()
    game.on_update_interval(randint(500, 1000), on_update_interval)
    game.on_update_interval(randint(500, 1000), on_update_interval2)


change_Scene("Battle")
