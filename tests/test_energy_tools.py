import sys
import os

sys.path.append(os.path.abspath("src"))

from energy_tools import calculate_energy, calculate_cost


def test_calculate_energy():
    assert calculate_energy(2, 5) == 12


def test_calculate_cost():
    assert calculate_cost(10, 0.3) == 3
