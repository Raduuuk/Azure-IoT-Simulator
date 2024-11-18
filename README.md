# Azure IoT Hub Data Simulator

## Overview
This project demonstrates an IoT solution that simulates a virtual sensor to generate and send temperature and humidity data to Azure IoT Hub. The data is routed to Azure Cosmos DB for storage and is visualized in Power BI.

## Features
- **Data Simulation**: Randomized temperature and humidity data generated every 15 seconds.
- **Azure IoT Hub Integration**: Data is sent to IoT Hub for processing.
- **Cosmos DB Storage**: Data is stored in Azure Cosmos DB in JSON format.
- **Real-time Visualization**: Data is visualized in Power BI for analysis.

## Setup Instructions

### Requirements
- Python 3.8+
- Azure account with:
  - Azure IoT Hub (Free Tier)
  - Azure Cosmos DB (SQL API)
- Power BI Desktop (for visualization)
- `azure-iot-device` library

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Raduuuk/Azure-IoT-Simulator.git
2. Navigate to the project directory:

   `cd Azure-IoT-Simulator`

3. Install required libraries:
   `pip install azure-iot-device`

## Usage
1. Open the script file `azure_iot.py` and replace `"CONNECTION_STRING"` with Azure IoT Hub device connection string.
2. Run the script:
`python azure_iot.py`
3. Configure the Cosmos DB routing in Azure IoT Hub:
    - Navigate to IoT Hub → Message Routing.
    - Add a route to Cosmos DB container.
4. Verify data in Cosmos DB:
    - Azure Portal → Cosmos DB → Data Explorer.
    - Open database and container to view incoming data.
5. Visualizing Data in Power BI:
    - Open Power BI Desktop and connect to Cosmos DB.
    - Use the Azure Cosmos DB (SQL API) connector.
    - Enter your URI and Primary Key from Cosmos DB.
    - Create visuals