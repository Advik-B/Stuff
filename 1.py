import pyglet
from pyglet.window import key

# window = pyglet.window.Window()
# image = pyglet.resource.image('dog.png')

# @window.event
# def on_draw():
#     window.clear()
#     image.blit(0, 0)

# @window.event
# def on_key_press(symbol, modifiers):
#     if symbol == key.LEFT:
#         print('left')
#     elif symbol == key.RIGHT:
#         print('right')
#     elif symbol == key.UP:
#         print('up')
#     elif symbol == key.DOWN:
#         print('down')

music = pyglet.resource.media('assets/music/Wii-music.mp3')
music.play()
pyglet.app.run()