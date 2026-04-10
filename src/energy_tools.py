"""
Simple utilities for basic energy calculations.

This module provides small helper functions to calculate
energy consumption and electricity costs based on
power usage and time.
"""


def     calculate_energy(power_kw: float, hours: float) -> float:
    """
    Calculate energy consumption in kilowatt-hours (kWh).

    Parameters
    ----------
    power_kw : float
        Power in kilowatts (kW).
    hours : float
        Operating time in hours (h).

    Returns
    -------
    float
        Energy consumption in kilowatt-hours (kWh).

    Example
    -------
    >>> calculate_energy(2, 5)
    10
    """
    return power_kw * hours


def calculate_cost(energy_kwh: float, price_per_kwh: float) -> float:
    """
    Calculate total electricity cost.

    Parameters
    ----------
    energy_kwh : float
        Energy consumption in kilowatt-hours (kWh).
    price_per_kwh : float
        Electricity price per kilowatt-hour (€/kWh).

    Returns
    -------
    float
        Total electricity cost.

    Example
    -------
    >>> calculate_cost(10, 0.3)
    3.0
    """
    return energy_kwh * price_per_kwh
