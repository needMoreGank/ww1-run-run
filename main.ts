// a function to switch scenes
// creates sprites/variables and CALLS functionns
function BattleSceneStart() {
    let index: number;
    
    scene.onHitWall(SpriteKind.Projectile, function on_hit_wall(sprite3: Sprite, location: tiles.Location) {
        sprite3.destroy()
    })
    sprites.onOverlap(SpriteKind.Player, MineSpriteKind, function on_on_overlap(sprite: Sprite, mine: Sprite) {
        
        hp = hp - 10
        if (hp == 0) {
            game.over(false)
        }
        
        statusbar.value = hp
        mine.destroy()
    })
    sprites.onOverlap(SpriteKind.Player, SpriteKind.Projectile, function on_on_overlap2(sprite2: Sprite, bullet: Sprite) {
        
        hp = hp - 20
        statusbar.value = hp
        if (hp == 0) {
            game.over(false)
        }
        
        bullet.destroy()
    })
    // 10/12
    // INSERT NEWSPAPER GAME SCENE CHANGE HERE!!
    sprites.onOverlap(SpriteKind.Player, NewsSpriteKind, function on_on_overlap3(sprite3: Sprite, newsScrap: Sprite) {
        
        newsScrap.destroy()
        news_count = news_count + 1
    })
    messenger = sprites.create(img`
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
        `, SpriteKind.Player)
    controller.moveSprite(messenger)
    scene.cameraFollowSprite(messenger)
    statusbar = statusbars.create(20, 4, StatusBarKind.Health)
    statusbar.attachToSprite(messenger)
    //  barbed_wire
    wire = sprites.create(img`
            f f f f 1 f f f f 1 f f f f f f 
                    f f f f 1 f f f f 1 f f 1 f f f 
                    f f f f 1 f f f 1 f f f 1 f f f 
                    f f f f 1 f f f 1 f f f 1 f f f 
                    f f 1 1 f f f 1 1 f f 1 f f f f 
                    f 1 f f f f f 1 f f f 1 f f f f 
                    f f f f f f f f f f f 1 f f f f 
                    f f f f f f f f f f f f f f f f
        `, SpriteKind.Enemy)
    wire.setPosition(30, 30)
    // 10/12
    newsScrap = sprites.create(img`
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
    `, NewsSpriteKind)
    scaling.scaleToPixels(wire, randint(32, 64), ScaleDirection.Horizontally, ScaleAnchor.Middle)
    for (index = 0; index < randint(6, 11); index++) {
        spawn_landmine()
    }
    for (index = 0; index < 5; index++) {
        spawn_newsScrap()
    }
    game.onUpdateInterval(randint(500, 1000), function on_update_interval() {
        
        leftBullet = sprites.create(img`
                . . . . . . . .
                                                        . . . . . . . .
                                                        . . . . . . . .
                                                        . 5 f 5 5 5 . .
                                                        . 5 f 5 5 5 5 .
                                                        . 5 f 5 5 5 . .
                                                        . . . . . . . .
                                                        . . . . . . . .
            `, SpriteKind.Projectile)
        leftBullet.setPosition(0, randint(16, 496))
        leftBullet.setVelocity(randint(60, 130), 0)
        leftBullet.startEffect(effects.trail)
    })
    game.onUpdateInterval(randint(500, 1000), function on_update_interval2() {
        
        rightBullet = sprites.create(img`
                . . . . . . . .
                                                            . . . . . . . .
                                                            . . . . . . . .
                                                            . 5 f 5 5 5 . .
                                                            . 5 f 5 5 5 5 .
                                                            . 5 f 5 5 5 . .
                                                            . . . . . . . .
                                                            . . . . . . . .
            `, SpriteKind.Projectile)
        rightBullet.setPosition(0, randint(16, 496))
        rightBullet.setVelocity(randint(60, 130), 0)
        rightBullet.startEffect(effects.trail)
    })
}

function IntroSceneStart() {
    
    duck = sprites.create(img`
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
        `, SpriteKind.Player)
    //  HOMEWORK!Walk left to talk to the duck and then switch to the battle scene
    scaling.scaleByPercent(duck, 50, ScaleDirection.Uniformly, ScaleAnchor.Middle)
    game.showLongText("Welcome to Time Travelling Co! Get to your work! (You may die)", DialogLayout.Bottom)
}

function PuzzleSceneStart() {
    game
}

function change_Scene(sceneName: string) {
    if (sceneName == "Intro") {
        tiles.setCurrentTilemap(introScene)
        IntroSceneStart()
    } else if (sceneName == "Battle") {
        tiles.setCurrentTilemap(battleScene)
        BattleSceneStart()
    } else if (sceneName == "Puzzle") {
        tiles.setCurrentTilemap(puzzleScene)
        PuzzleSceneStart()
    }
    
}

function spawn_landmine() {
    
    landmine = sprites.create(img`
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
        `, MineSpriteKind)
    landmine.setPosition(randint(16, 144), randint(16, 496))
}

// 10/12
function spawn_newsScrap() {
    
    newsScrap = sprites.create(img`
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
        `, NewsSpriteKind)
    newsScrap.setPosition(randint(16, 144), randint(16, 496))
}

// BINDING DUMP
let landmine : Sprite = null
let duck : Sprite = null
let wire : Sprite = null
let messenger : Sprite = null
let newsScrap : Sprite = null
let puzzleScene : tiles.TileMapData = null
let introScene : tiles.TileMapData = null
let battleScene : tiles.TileMapData = null
let rightBullet : Sprite = null
let leftBullet : Sprite = null
let statusbar : StatusBarSprite = null
battleScene = tilemap`
    level1
`
introScene = tilemap`
    level5
`
puzzleScene = tilemap`
    level6
`
let currentScene = "Battle"
let MineSpriteKind = SpriteKind.create()
let NewsSpriteKind = SpriteKind.create()
let hp_max = 100
let hp = hp_max
change_Scene("Intro")
// 10/12
let news_count = 0
