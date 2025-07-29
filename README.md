# airvisual1 MCP Server README

## Overview

The `airvisual1` MCP (Model Context Protocal) server provides a comprehensive suite of tools to access public data related to air quality, weather information, and health recommendations. It delivers live data synchronized with the official site, ensuring that you receive the most up-to-date information upon request.

## Features

- **Real-Time Data Access**: Fetch real-time air pollution data, weather information, and health recommendations.
- **Comprehensive Coverage**: Access almost everything that is publicly available on the official site.
- **Dynamic Querying**: Request data on demand without the need for local caching or storage.

## Tool List

The server is organized into several functional groups, each containing specific tools to handle different types of data requests:

### Auto-Complete Tools
- **v2/auto-complete**: Find countries, cities, and places by name.
- **places/v2/list**: List places with brief information.
- **places/v2/list-by-map**: List places in a specified area by providing boundary coordinates.

### Station Information Tools
- **stations/v2/get-information**: Fetch detailed information from a specific station using its ID.
- **stations/v2/get-measurements**: Retrieve measurement data from a specific station using its ID.

## Tool Details

### Auto-Complete Tools

- **v2_auto_complete**:
  - Find locations by name.
  - Optional parameters include user language, timezone, AQI index, and units for pressure, distance, and temperature.

- **v2_list**:
  - List places with brief information.
  - Optional parameters include language, timezone, AQI index, and units for pressure, distance, and temperature.

- **v2_list_by_map**:
  - List places in an area by providing a boundary box.
  - Required parameters include boundary coordinates (NElon, SWlon, SWlat, NElat).
  - Optional parameters include language, timezone, AQI index, and units for pressure, distance, and temperature.

### Station Information Tools

- **v2_get_information**:
  - Retrieve information from a station using its ID.
  - Optional parameters include user language, AQI index, timezone, and units for pressure, distance, and temperature.

- **v2_get_measurements**:
  - Obtain measurements from a station using its ID.
  - Optional parameters include user language, AQI index, timezone, and units for pressure, distance, and temperature.

## Conclusion

The `airvisual1` MCP server is a powerful tool for accessing live environmental data. Its comprehensive suite of tools allows for detailed querying and retrieval of air quality and weather-related information, making it an essential resource for developers and researchers interested in environmental data.
