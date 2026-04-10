import numpy as np
from indices import ILWI, CWI, GMI, AMI, classify_pixel

# Example pixel reflectance values (dummy)
B2, B3, B4 = 0.05, 0.06, 0.04
B6, B7 = 0.03, 0.02
B8, B8A = 0.01, 0.005
B9 = 0.002

ilwi = ILWI(B6, B7, B8, B8A)
cwi = CWI(B2, B3, B6, B7, B8, B8A, B9)
gmi = GMI(B2, B3, B4, B8)
ami = AMI(B8A, B6)

classification = classify_pixel(ilwi, cwi, gmi, ami)

print("Classification:", classification)
