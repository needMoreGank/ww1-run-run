
#a function to switch scenes
#creates sprites/variables and CALLS functionns
def BattleSceneStart():
    global messenger, statusbar, wire, newsScrap, news_count
    
    def on_hit_wall(sprite3, location):
        sprite3.destroy()
    scene.on_hit_wall(SpriteKind.projectile, on_hit_wall)
    
    
    def on_on_overlap(sprite, mine):
        global hp
        hp = hp - 10
        if hp == 0:
            game.over(False)
        statusbar.value = hp
        mine.destroy()
    sprites.on_overlap(SpriteKind.player, MineSpriteKind, on_on_overlap)
    
    
    def on_on_overlap2(sprite2, bullet):
        global hp
        hp = hp - 20
        statusbar.value = hp
        if hp == 0:
            game.over(False)
        bullet.destroy()
    sprites.on_overlap(SpriteKind.player, SpriteKind.projectile, on_on_overlap2)

    #10/12
    def on_on_overlap3(sprite3, newsScrap):
        global news_count
        newsScrap.destroy()
        news_count = news_count + 1
        #INSERT NEWSPAPER GAME SCENE CHANGE HERE!!
    sprites.on_overlap(SpriteKind.player, NewsSpriteKind, on_on_overlap3)
    
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

    #10/12
    newsScrap = sprites.create(img("""
        . . . . . . . . . . . . . . . .
        . . . . . . . 1 1 1 . . . . . .
        . . . . . 1 1 1 1 1 1 . . . . .
        . . . . 1 1 1 1 f 1 1 . . . . .
        . . . 1 1 1 f f 1 1 1 . . . . .
        . . 1 1 1 f 1 1 1 1 1 1 . . . .
        . 1 1 f f 1 1 1 1 1 1 1 1 . . .
        . 1 1 f 1 1 1 1 1 1 1 1 1 . . .
        . 1 1 1 1 1 1 1 1 1 1 1 1 1 . .
        . 1 1 d d 1 1 1 1 1 1 1 1 d . .
        . . d d . d 1 1 1 1 1 1 d . . .
        . . . . d d 1 1 1 1 1 1 1 d . .
        . . . . d 1 1 1 1 1 1 1 1 . . .
        . . . . 1 1 1 1 1 1 . . . . . .
        . . . . 1 1 1 1 . . . . . . . .
        . . . . . 1 . . . . . . . . . .
    """), NewsSpriteKind)

    scaling.scale_to_pixels(wire,
        randint(32, 64),
        ScaleDirection.HORIZONTALLY,
        ScaleAnchor.MIDDLE)
    for index in range(randint(6, 11)):
        spawn_landmine()
    
    for index in range(5):
        spawn_newsScrap()
    
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
    game.on_update_interval(randint(500, 1000), on_update_interval)
    
    
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
    game.on_update_interval(randint(500, 1000), on_update_interval2)
    
def IntroSceneStart():
    global duck, messenger
    duck = sprites.create(img("""
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
    """),
        SpriteKind.player)
    # HOMEWORK!Walk left to talk to the duck and then switch to the battle scene
    scaling.scale_by_percent(duck, 50, ScaleDirection.UNIFORMLY, ScaleAnchor.MIDDLE)
    
    controller.move_sprite(messenger)
    messenger.setPosition(240, 64)
    controller.A.on_event(ControllerButtonEvent.PRESSED, on_event_pressed)  

def on_event_pressed():
    global duck, messenger
    if (abs(messenger.x - duck.x) < 5 ):
        if (abs(messenger.y - duck.y) < 5 ):
            game.show_long_text("Welcome to Time Travelling Co! Get to work! (You might die)", DialogLayout.BOTTOM)


def PuzzleSceneStart():
    pass
    #insert game here
def change_Scene(sceneName: str):
    if sceneName == "Intro":
        tiles.set_current_tilemap(introScene)
        IntroSceneStart()
    elif sceneName == "Battle":
        tiles.set_current_tilemap(battleScene)
        BattleSceneStart()
    elif sceneName == "Puzzle":
        tiles.set_current_tilemap(puzzleScene)
        PuzzleSceneStart()
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

#10/12
def spawn_newsScrap():
    global newsScrap
    newsScrap = sprites.create(img("""
            . . . . . . . . . . . . . . . .
            . . . . . . . 1 1 1 . . . . . .
            . . . . . 1 1 1 1 1 1 . . . . .
            . . . . 1 1 1 1 f 1 1 . . . . .
            . . . 1 1 1 f f 1 1 1 . . . . .
            . . 1 1 1 f 1 1 1 1 1 1 . . . .
            . 1 1 f f 1 1 1 1 1 1 1 1 . . .
            . 1 1 f 1 1 1 1 1 1 1 1 1 . . .
            . 1 1 1 1 1 1 1 1 1 1 1 1 1 . .
            . 1 1 d d 1 1 1 1 1 1 1 1 d . .
            . . d d . d 1 1 1 1 1 1 d . . .
            . . . . d d 1 1 1 1 1 1 1 d . .
            . . . . d 1 1 1 1 1 1 1 1 . . .
            . . . . 1 1 1 1 1 1 . . . . . .
            . . . . 1 1 1 1 . . . . . . . .
            . . . . . 1 . . . . . . . . . .
        """), NewsSpriteKind)
    newsScrap.set_position(randint(16, 144), randint(16, 496))


#BINDING DUMP
landmine: Sprite = None
duck: Sprite = None
wire: Sprite = None
messenger: Sprite = None
newsScrap: Sprite = None
puzzleScene: tiles.TileMapData = None
introScene: tiles.TileMapData = None
battleScene: tiles.TileMapData = None
rightBullet: Sprite = None
leftBullet: Sprite = None
statusbar: StatusBarSprite = None
battleScene = tilemap("""
    level1
""")
introScene = tilemap("""level5""")
puzzleScene = tilemap("""
    level6
""")
currentScene = "Battle"
MineSpriteKind = SpriteKind.create()
NewsSpriteKind = SpriteKind.create()
hp_max = 100
hp = hp_max
change_Scene("Intro")

#10/12
news_count = 0