import pygame
from functions import read_osu_map
from tkinter.filedialog import askopenfilename
from os import makedirs
from os.path import join, dirname, isfile
import json, shutil, sys

WINDOW_WIDTH, WINDOW_LENGTH = 1080, 720
LINE_HEIGHT = 550
