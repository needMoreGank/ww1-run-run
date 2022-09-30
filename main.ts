sprites.onOverlap(SpriteKind.Player, SpriteKind.Projectile, function on_on_overlap(sprite: Sprite, otherSprite: Sprite) {
    game.over(false)
})
//  tile size is 16*16
tiles.setCurrentTilemap(tilemap`
    level2
`)
//  HW:
//  Sprite design ART
//  barbed wire, mine, bullet, blood, random stuff
//  research trenches FOR REAL TO SEE IF IT WORKS
//  GITHUB AGAINST
let hp_max = 100
let hp_current = hp_max
let messenger = sprites.create(img`
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
let currentScene = "game"
controller.moveSprite(messenger)
scene.cameraFollowSprite(messenger)
