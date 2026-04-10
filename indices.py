import numpy as np

# NOTE: These functions assume reflectance arrays as input

def ILWI(B6, B7, B8, B8A):
    """Improved Land-Water Index"""
    return (B6 + B7) - 1.5 * (B8 + B8A)

def CWI(B2, B3, B6, B7, B8, B8A, B9):
    """Clear Water Index"""
    return -100 * ((B2 + B3) - (B6 + B7 + B8 + B8A + B9))

def GMI(B2, B3, B4, B8):
    """Glint Mapping Index"""
    return (B8 - B4) / (B2 + B3)

def AMI(B8A, B6):
    """Adjacency Mapping Index"""
    return (B6 - B8A)

# Threshold-based classification
def classify_pixel(ilwi, cwi, gmi, ami):
    if ilwi < 0.8:
        return "land"

    if cwi >= 1:
        return "clear_water"

    if -1 < cwi < 1:
        if gmi >= 0.05:
            return "glint"
        else:
            return "bottom"

    if cwi <= -1:
        if ami >= 0.05:
            return "adjacency"
        else:
            return "bottom"

    return "unknown"
