from pprint import pprint

from shapely.geometry import Polygon

from predict import save_forest_prediction_to_geotiff, predict_forest

from pprint import pprint

# Example usage:
if __name__ == "__main__":
    # Example AOI Brno
    aoi_parts = [
        [16.60806452202965, 49.20805887025071],
        [16.60667266444227, 49.20764317925989],
        [16.607060396198165, 49.2066039364926],
        [16.608094347549496, 49.2064675342576],
        [16.608889694743056, 49.20679230086469],
        [16.60874056714377, 49.20781854932278],
        [16.60806452202965, 49.20805887025071]
    ]
    # Convert the list of coordinates to a Polygon
    aoi = Polygon(aoi_parts)
    # Define the CRS (Coordinate Reference System)
    crs = "EPSG:32633"  # UTM Zone 33N

    # Call the function to predict forest cover
    result = predict_forest(
        aoi=aoi,
        crs=crs
    )

    pprint(result)

    # Optional: Save the prediction result to a GeoTIFF file
    save_forest_prediction_to_geotiff(
        result=result,
        output_path="forest_prediction.tif",
        crs=crs
    )
