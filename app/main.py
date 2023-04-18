from nicegui import ui

with ui.scene(width=1400, height=200) as scene:
    with scene.group().move(0, 0, 1):
        scene.text("A sphere").move(0, 0, 2)
        scene.sphere().material(color="#4488ff")
        with scene.group().move(3, 0, 0):
            scene.text("a box").move(0, 0, 2)
            scene.box().scale(2, 1, 1).rotate(0, 5, 0)
ui.run(port=8000)
