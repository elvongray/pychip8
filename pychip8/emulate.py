"""
The main process
"""
import os
from functools import partial

from cpu.cpu import Chip8
from display_unit.renderer import app

chip8 = Chip8()
chip8.initialize()

loaded_program = []

with open('%s/pychip8/roms/BLINKY' % (os.getcwd()), 'r') as file:
    for byte in iter(partial(file.read, 1), b''):
        loaded_program.append(ord(byte))

chip8.load_program(loaded_program)

chip8.set_renderer(app)

app.initialize_screen()

chip8.emulate_cpu()
