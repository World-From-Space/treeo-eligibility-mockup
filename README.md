# treeo_mockup

A minimal Python mockup to generate dummy forest cover predictions as a GeoTIFF for a given shapely polygon.

## Requirements

- Python 3.6+
- numpy
- shapely
- rasterio

## Installation & Usage

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python main.py
```

The script `main.py` demonstrates calling `predict_forest` and saving the result to `forest_prediction.tif`.