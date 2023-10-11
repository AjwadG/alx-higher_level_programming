#!/usr/bin/python3


def roman_to_int(roman_string):
    if not roman_string or not isinstance(roman_string, str):
        return 0
    rom_double = {"IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900}
    rom = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    suma = 0
    i = 0
    while i < len(roman_string):
        if roman_string[i: i + 2] in rom_double:
            suma += rom_double[roman_string[i: i + 2]]
            i += 1
        elif roman_string[i] in rom:
            suma += rom[roman_string[i]]
        else:
            return 0
        i += 1
    return suma
