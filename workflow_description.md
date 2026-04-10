## Workflow Description

The workflow applies a hierarchical classification:

1. ILWI → separates land and water
2. CWI → separates optically deep and disturbed water
3. GMI → identifies surface glint
4. AMI → identifies adjacency effects

Thresholds:
- ILWI ≥ 0.8 → water
- CWI ≥ 1 → clear water
- -1 < CWI < 1 → disturbed water
- CWI ≤ -1 → adjacency-dominated
- GMI ≥ 0.05 → glint
- AMI ≥ 0.05 → adjacency
