tiles.setCurrentTilemap(tilemap`level1`)
//  tile size is 1enum)s FOR REAL TO SEE IF IT WORKS
//  GITHUB AGAINST
// enum = 
let hp_max = 100
let hp = hp_max
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
game.onUpdateInterval(randint(500, 1000), function spawn_leftBullet() {
    let leftBullet = sprites.create(img`
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
game.onUpdateInterval(randint(500, 1000), function spawn_rightBullet() {
    let rightBullet = sprites.create(img`
        . . . . . . . .
        . . . . . . . .
        . . . . . . . .
        . . 5 5 5 f 5 .
        . 5 5 5 5 f 5 .
        . . 5 5 5 f 5 .
        . . . . . . . .
        . . . . . . . .
    `, SpriteKind.Projectile)
    rightBullet.setPosition(270, randint(16, 496))
    rightBullet.setVelocity(randint(-60, -130), 0)
    rightBullet.startEffect(effects.trail)
})
scene.onHitWall(SpriteKind.Projectile, function on_hit_wall(sprite: Sprite, location: tiles.Location) {
    sprite.destroy()
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Projectile, function hit_bullet(sprite: Sprite, bullet: Sprite) {
    
    hp = hp - 20
    if (hp == 0) {
        game.over(false)
    }
    
    bullet.destroy()
})
// barbed_wire
let wire = sprites.create(img`
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
scaling.scaleToPixels(wire, randint(32, 64), ScaleDirection.Horizontally, ScaleAnchor.Middle)
// landmine
let landmine = sprites.create(img`
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
`, SpriteKind.Enemy)
