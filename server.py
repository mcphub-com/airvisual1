import requests
from datetime import datetime
from typing import Union, Literal, List
from mcp.server import FastMCP
from pydantic import Field
from typing import Annotated
from mcp.server.fastmcp import FastMCP
from fastmcp import FastMCP, Context
import os
from dotenv import load_dotenv
load_dotenv()
rapid_api_key = os.getenv("RAPID_API_KEY")

__rapidapi_url__ = 'https://rapidapi.com/apidojo/api/airvisual1'

mcp = FastMCP('airvisual1')

@mcp.tool()
def v2_auto_complete(q: Annotated[str, Field(description='Name of countries, cities, districts, places, etc...')],
                     x_user_lang: Annotated[Union[str, None], Field(description='')] = None,
                     x_user_timezone: Annotated[Union[str, None], Field(description='')] = None,
                     x_aqi_index: Annotated[Union[str, None], Field(description='One of the following : us|cn')] = None,
                     x_units_pressure: Annotated[Union[str, None], Field(description='One of the following : hg|mbar')] = None,
                     x_units_distance: Annotated[Union[str, None], Field(description='One of the following : miles|kilometer')] = None,
                     x_units_temperature: Annotated[Union[str, None], Field(description='One of the following : fahrenheit|celsius')] = None) -> dict: 
    '''Find countries, cities, places by name'''
    url = 'https://airvisual1.p.rapidapi.com/v2/auto-complete'
    headers = {'x-rapidapi-host': 'airvisual1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'q': q,
        'x-user-lang': x_user_lang,
        'x-user-timezone': x_user_timezone,
        'x-aqi-index': x_aqi_index,
        'x-units-pressure': x_units_pressure,
        'x-units-distance': x_units_distance,
        'x-units-temperature': x_units_temperature,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def v2_list(data: Annotated[dict, Field(description='')] = None) -> dict: 
    '''List places with brief information'''
    url = 'https://airvisual1.p.rapidapi.com/places/v2/list'
    headers = {'Content-Type': 'application/json', 'x-rapidapi-host': 'airvisual1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    response = requests.post(url, headers=headers, json=data)
    return response.json()

@mcp.tool()
def v2_list_by_map(NElon: Annotated[Union[int, float], Field(description='North East longitude of boundary Default: -73.43762621283531')],
                   SWlon: Annotated[Union[int, float], Field(description='Sount West longitude of boundary Default: -74.41956583410503')],
                   SWlat: Annotated[Union[int, float], Field(description='Sount West latitude of boundary Default: 40.43539120253853')],
                   NElat: Annotated[Union[int, float], Field(description='North East latitude of boundary Default: 40.95240778688068')],
                   x_user_lang: Annotated[Union[str, None], Field(description='')] = None,
                   x_user_timezone: Annotated[Union[str, None], Field(description='')] = None,
                   x_aqi_index: Annotated[Union[str, None], Field(description='One of the following : us|cn')] = None,
                   x_units_pressure: Annotated[Union[str, None], Field(description='One of the following : hg|mbar')] = None,
                   x_units_distance: Annotated[Union[str, None], Field(description='One of the following : miles|kilometer')] = None,
                   x_units_temperature: Annotated[Union[str, None], Field(description='One of the following : fahrenheit|celsius')] = None) -> dict: 
    '''List places in an area by providing a boundary box'''
    url = 'https://airvisual1.p.rapidapi.com/places/v2/list-by-map'
    headers = {'x-rapidapi-host': 'airvisual1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'NElon': NElon,
        'SWlon': SWlon,
        'SWlat': SWlat,
        'NElat': NElat,
        'x-user-lang': x_user_lang,
        'x-user-timezone': x_user_timezone,
        'x-aqi-index': x_aqi_index,
        'x-units-pressure': x_units_pressure,
        'x-units-distance': x_units_distance,
        'x-units-temperature': x_units_temperature,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def auto_complete(query: Annotated[str, Field(description='Name of countries, cities, districts, places, etc...')]) -> dict: 
    '''Find countries, cities, places by name'''
    url = 'https://airvisual1.p.rapidapi.com/auto-complete'
    headers = {'x-rapidapi-host': 'airvisual1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'query': query,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def places_list(data: Annotated[dict, Field(description='')] = None) -> dict: 
    '''List places with brief information'''
    url = 'https://airvisual1.p.rapidapi.com/places/list'
    headers = {'Content-Type': 'application/json', 'x-rapidapi-host': 'airvisual1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    response = requests.post(url, headers=headers, json=data)
    return response.json()

@mcp.tool()
def places_list_by_map(NElon: Annotated[Union[int, float], Field(description='North East longitude of boundary Default: -73.43762621283531')],
                       SWlon: Annotated[Union[int, float], Field(description='Sount West longitude of boundary Default: -74.41956583410503')],
                       mapType: Annotated[str, Field(description='GoogleMap or China is allowed')],
                       SWlat: Annotated[Union[int, float], Field(description='Sount West latitude of boundary Default: 40.43539120253853')],
                       NElat: Annotated[Union[int, float], Field(description='North East latitude of boundary Default: 40.95240778688068')],
                       zoomLevel: Annotated[Union[int, float], Field(description='Zoom level of map, this value affects how many places returned in response Default: 9')],
                       aqiIndex: Annotated[Union[str, None], Field(description='AQI index (us | cn)')] = None,
                       lang: Annotated[Union[str, None], Field(description='Language code')] = None,
                       timezone: Annotated[Union[str, None], Field(description='Timezone')] = None) -> dict: 
    '''List places in an area by providing a boundary box'''
    url = 'https://airvisual1.p.rapidapi.com/places/list-by-map'
    headers = {'x-rapidapi-host': 'airvisual1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'NElon': NElon,
        'SWlon': SWlon,
        'mapType': mapType,
        'SWlat': SWlat,
        'NElat': NElat,
        'zoomLevel': zoomLevel,
        'aqiIndex': aqiIndex,
        'lang': lang,
        'timezone': timezone,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def v2_get_information(id: Annotated[str, Field(description='The value of id field (type is station) that returned in …/v2/auto-complete endpoint')],
                       x_user_lang: Annotated[Union[str, None], Field(description='')] = None,
                       x_aqi_index: Annotated[Union[str, None], Field(description='One of the following : us|cn')] = None,
                       x_units_pressure: Annotated[Union[str, None], Field(description='One of the following : hg|mbar')] = None,
                       x_units_distance: Annotated[Union[str, None], Field(description='One of the following : miles|kilometer')] = None,
                       x_user_timezone: Annotated[Union[str, None], Field(description='')] = None,
                       x_units_temperature: Annotated[Union[str, None], Field(description='One of the following : fahrenheit|celsius')] = None) -> dict: 
    '''Get information at specific station by its id'''
    url = 'https://airvisual1.p.rapidapi.com/stations/v2/get-information'
    headers = {'x-rapidapi-host': 'airvisual1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
        'x-user-lang': x_user_lang,
        'x-aqi-index': x_aqi_index,
        'x-units-pressure': x_units_pressure,
        'x-units-distance': x_units_distance,
        'x-user-timezone': x_user_timezone,
        'x-units-temperature': x_units_temperature,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def v2_get_measurements(id: Annotated[str, Field(description='The value of id field (type is station) that returned in …/v2/auto-complete endpoint')],
                        x_user_lang: Annotated[Union[str, None], Field(description='')] = None,
                        x_aqi_index: Annotated[Union[str, None], Field(description='One of the following : us|cn')] = None,
                        x_units_pressure: Annotated[Union[str, None], Field(description='One of the following : hg|mbar')] = None,
                        x_units_distance: Annotated[Union[str, None], Field(description='One of the following : miles|kilometer')] = None,
                        x_user_timezone: Annotated[Union[str, None], Field(description='')] = None,
                        x_units_temperature: Annotated[Union[str, None], Field(description='One of the following : fahrenheit|celsius')] = None) -> dict: 
    '''Get measurements at specific station by its id'''
    url = 'https://airvisual1.p.rapidapi.com/stations/v2/get-measurements'
    headers = {'x-rapidapi-host': 'airvisual1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
        'x-user-lang': x_user_lang,
        'x-aqi-index': x_aqi_index,
        'x-units-pressure': x_units_pressure,
        'x-units-distance': x_units_distance,
        'x-user-timezone': x_user_timezone,
        'x-units-temperature': x_units_temperature,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def stations_get_information(id: Annotated[str, Field(description='The value of id field (type is station) that received from .../auto-complete API')],
                             lang: Annotated[Union[str, None], Field(description='')] = None,
                             aqiIndex: Annotated[Union[str, None], Field(description='AQI index (us | cn)')] = None,
                             timezone: Annotated[Union[str, None], Field(description='')] = None) -> dict: 
    '''Get information at specific station by its id'''
    url = 'https://airvisual1.p.rapidapi.com/stations/get-information'
    headers = {'x-rapidapi-host': 'airvisual1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
        'lang': lang,
        'aqiIndex': aqiIndex,
        'timezone': timezone,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def stations_get_measurements(id: Annotated[str, Field(description='The value of id field (type is station) that received from .../auto-complete API')],
                              timezone: Annotated[Union[str, None], Field(description='')] = None,
                              aqiIndex: Annotated[Union[str, None], Field(description='AQI index (us | cn)')] = None,
                              lang: Annotated[Union[str, None], Field(description='')] = None) -> dict: 
    '''Get measurements at specific station by its id'''
    url = 'https://airvisual1.p.rapidapi.com/stations/get-measurements'
    headers = {'x-rapidapi-host': 'airvisual1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
        'timezone': timezone,
        'aqiIndex': aqiIndex,
        'lang': lang,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()



if __name__ == '__main__':
    import sys
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 9997
    mcp.run(transport="stdio")
