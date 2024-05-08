import pandas as pd
import geopandas as gpd

from helpers import *

config_data = load_config()

def get_polygons(
        file_path: str = '../data/geospatial/PAK-admin-zones.geojson',
        crs: int = 4326,
        by: str = 'ADM1_EN',
):
    return (
        gpd
        .read_file(file_path)
        .to_crs(crs=crs)
        .dissolve(by=by)
        .reset_index()
    )


def get_centroids(
        file_path: str = '../data/geospatial/PAK-admin-zones.geojson',
        crs: int = 4326,
        by: str = 'ADM1_EN',
):
    polygons = get_polygons(file_path, crs, by)
    nodes = polygons.set_index(['ADM1_PCODE','ADM1_EN']).centroid.reset_index()
    nodes['latitude'] = nodes[0].y
    nodes['longitude'] = nodes[0].x
    nodes.to_csv('../data/_MODEL_INPUTS/nodes.csv', index=False)
    return nodes.drop(0, axis=1)


def get_powerplants(
        file_path: str = '../data/power-plants/PAK-power-plants.csv',
        crs: int = 4326,
):
    include_captive_plants = config_data['include_captive_plants']
    operating_status = config_data['operating_status']
    power_plants = (
        pd
        .read_csv(file_path)
        .query( f'is_captive == {include_captive_plants}' )
        .query( f'operating_status.isin({operating_status})' )
    )
    return ( 
        gpd.GeoDataFrame(
            geometry=gpd.points_from_xy(
            power_plants.longitude, 
            power_plants.latitude, 
            crs=f'EPSG:{crs}'
            ), 
            data=power_plants
        )
    )


def sjoin_powerplants(
        iso_code: str,
):
    polygons = get_polygons(file_path = f'../data/geospatial/{iso_code}-admin-zones.geojson')
    power_plants = get_powerplants(file_path = f'../data/power-plants/{iso_code}-power-plants.csv')
    return (
        gpd
        .sjoin(
            power_plants, 
            polygons[['ADM1_EN','ADM1_PCODE','geometry']], 
            how='inner', 
            predicate='within'
        )
    )