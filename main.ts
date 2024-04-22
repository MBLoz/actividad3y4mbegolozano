scene.setBackgroundColor(12)
tiles.setCurrentTilemap(tilemap`level0`)
game.splash("Consigue monedas")
let persona2 = sprites.create(assets.image`persona1`, SpriteKind.Player)
animation.runImageAnimation(
persona2,
assets.animation`persona2myAnim`,
200,
true
)
persona2.setPosition(16, 31)
