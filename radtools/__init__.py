# RAD-tools - program for spin Hamiltonian and magnons.
# Copyright (C) 2022-2023  Andrey Rybakov
# 
# e-mail: anry@uv.es, web: adrybakov.com

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

r"""
RAD-tools
"""


__version__ = "0.8.5"
__doclink__ = "rad-tools.org"
__git_hash__ = "9679f7a85c201fe15b2c52edd24cc7c4f8b95df1"
__release_date__ = "25 September 2023"

from . import (
    constants,
    crystal,
    decorate,
    dos,
    exceptions,
    geometry,
    io,
    magnons,
    numerical,
    score,
    spinham,
)
from .constants import *
from .crystal import *
from .decorate import *
from .dos import *
from .geometry import *
from .io import *
from .magnons import *
from .numerical import *
from .score import *
from .spinham import *

__all__ = ["__version__", "__doclink__", "__git_hash__", "__release_date__"]
__all__.extend(crystal.__all__)
__all__.extend(decorate.__all__)
__all__.extend(dos.__all__)
__all__.extend(spinham.__all__)
__all__.extend(io.__all__)
__all__.extend(magnons.__all__)
__all__.extend(score.__all__)
__all__.extend(constants.__all__)
__all__.extend(geometry.__all__)
__all__.extend(numerical.__all__)
