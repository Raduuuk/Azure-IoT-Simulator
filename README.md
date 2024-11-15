# Azure IoT Hub Data Simulator

This project simulates an IoT device sending temperature and humidity data to Azure IoT Hub. The script generates random temperature and humidity readings and sends them to Azure IoT Hub via the IoT SDK.

## Project Setup

### Requirements
- Python 3.6+
- Azure IoT Hub account
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
1. Open the script file `azure_iot.py` and replace `"YOUR_PRIMARY_CONNECTION_STRING"` with your Azure IoT Hub device connection string.
2. Run the script:
`python azure_iot.py`
