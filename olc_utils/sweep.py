# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/02_sweep.ipynb.

# %% auto 0
__all__ = ['get_max_min_chars', 'get_right_diagonal_vertex_grids']

# %% ../nbs/02_sweep.ipynb 3
import pandas as pd
from openlocationcode import openlocationcode as olc
from .grid import *
from typing import Tuple

# %% ../nbs/02_sweep.ipynb 6
def get_max_min_chars(
    str1: str,
    str2: str,
) -> Tuple[str, str]:
    max_str = ""
    min_str = ""
    for i in range(len(str1)):
        if str1[i] == str2[i]:
            max_str += str1[i]
            min_str += str1[i]

        elif olc.CODE_ALPHABET_.index(str1[i]) > olc.CODE_ALPHABET_.index(str2[i]):
            max_str += str1[i:]
            min_str += str2[i:]
            break
        else:
            max_str += str2[i:]
            min_str += str1[i:]
            break

    return max_str, min_str

# %% ../nbs/02_sweep.ipynb 9
def get_right_diagonal_vertex_grids(
    grid1: str,
    grid2: str,
)-> Tuple[str, str]:
    if len(grid1) != len(grid2):
        raise ValueError("Grids must be of the same length")

    # Get the characters for X axis
    x_grid_1 = ''.join([x for i, x in enumerate(grid1) if i % 2 == 1])
    x_grid_2 = ''.join([x for i, x in enumerate(grid2) if i % 2 == 1])

    # Get the characters for Y axis
    y_grid_1 = ''.join([x for i, x in enumerate(grid1) if i % 2 == 0])
    y_grid_2 = ''.join([x for i, x in enumerate(grid2) if i % 2 == 0])
    
    # Calculate the X max & min characters
    x_max_grid, x_min_grid = get_max_min_chars(x_grid_1, x_grid_2)
    y_max_grid, y_min_grid = get_max_min_chars(y_grid_1, y_grid_2)
    
    left_bottom = ''.join(''.join(tup) for tup in zip(y_min_grid, x_min_grid))
    right_top =  ''.join(''.join(tup) for tup in zip(y_max_grid, x_max_grid))
    
    return left_bottom, right_top