scene.set_background_color(12)
tiles.set_current_tilemap(tilemap("""
    level0
"""))
game.splash("Consigue monedas")
persona2 = sprites.create(assets.image("""
    persona1
"""), SpriteKind.player)
animation.run_image_animation(persona2,
    assets.animation("""
        persona2myAnim
    """),
    200,
    True)
persona2.set_position(16, 31)