# GlintMapper Workflow

This repository provides a minimal implementation and documentation of the multi-index workflow described in:

**Soomets et al. (2026)**  
_Disentangling dominant near-shore Sentinel-2 reflectance contributions from water, bottom, adjacency, and surface glint_  
Submitted to *International Journal of Applied Earth Observation and Geoinformation (JAG)*.

---

## Overview

The workflow is designed to classify dominant signal contributions in optically complex near-shore waters using Sentinel-2 top-of-atmosphere (TOA) reflectance.

The method partitions pixels into:
- Land
- Optically deep (clear) water
- Bottom-influenced water
- Adjacency-affected water
- Surface glint

The approach is based on spectral indices and threshold-based classification.

---

## Workflow Steps

1. Land–water separation (ILWI)
2. Clear vs disturbed water classification (CWI)
3. Glint detection (GMI)
4. Adjacency detection (AMI)

---

## Data Requirements

- Sentinel-2 Level-1C TOA reflectance data
- Bands: B2–B9 (visible, red-edge, NIR)
- Spatial resolution: 10–20 m

Data can be downloaded from:
https://dataspace.copernicus.eu/

---

## Reproducibility

All indices and thresholds are fully described in the manuscript.  
This repository provides a minimal Python implementation for demonstration purposes.

---

## Disclaimer

This implementation is intended as a conceptual demonstration of the workflow.  
It is not a fully operational processing pipeline.

---

## Contact

Tuuli Soomets  
Estonian Marine Institute, University of Tartu  
