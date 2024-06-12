# Aircraft Digital Twin Simulator

## Overview

This project was developed for academic purposes as part of an assignment on generative AI. The objective was to identify an industry where generative AI could have a significant impact. We chose the aircraft manufacturing industry, focusing on the use case of digital twins powered by generative AI. This text-based prototype aims to demonstrate how generative AI can be leveraged to create digital twins that assist in aircraft maintenance and operations.

## Project Description

The **Aircraft Digital Twin Simulator** is a proof-of-concept application that simulates the functionality of a digital twin for aircraft maintenance. By inputting an aircraft ID, users can receive a summary of the aircraft's status, detect potential anomalies, and get recommendations for maintenance. This prototype showcases the potential of generative AI in transforming aircraft maintenance processes.

## Features

- **Aircraft Status Summary**: Provides a brief overview of the aircraft's operational state.
- **Anomaly Detection**: Lists potential anomalies detected in the aircraft.
- **Maintenance Recommendations**: Offers additional maintenance needs or recommendations based on the status and detected anomalies.

## Getting Started

### Prerequisites

- Python 3.8 or higher
- Poetry (for dependency management)

### Installation

1. **Clone the repository:**

   ```bash
   git clone <repository-url>
   cd aircraft-digital-twin-simulator
   ```
2. **Set up the Poetry environment:**

   ```bash
   poetry install
   ```

3. **Create a `.env` file:**

    Create a `.env` file in the root directory with your Azure OpenAI API credentials:
    
    ```plaintext
    AZURE_OPENAI_API_KEY=your_api_key
    AZURE_OPENAI_ENDPOINT=your_endpoint
    AZURE_OPENAI_DEPLOYMENT=your_deployment
   ```

### Running the Application

1. **Run the streamlit app locally:**

   ```bash
   poetry run streamlit run streamlit_app/app.py
   ```
## Project Structure

- `aircraft_digital_twin_simulator/`: Contains the core application logic.
- `streamlit_app/`: Contains the Streamlit app for the user interface.
- `.env`: Environment variables file (should not be committed to version control).
- `requirements.txt`: List of dependencies (if needed for compatibility with some platforms).
- `pyproject.toml`: Poetry configuration file.
- `poetry.lock`: Poetry lock file.
- `README.md`: Setup instructions and project documentation.

## Deployment

This application can be deployed using Streamlit Cloud or other deployment platforms like Heroku. Ensure that environment variables are set appropriately in the deployment settings.

## Academic Context

This project was built for academic purposes as part of an assignment to explore the disruptive potential of generative AI in various industries. We chose the aircraft manufacturing industry and focused on the use case of AI-powered digital twins. This prototype provides a glimpse into how such technology can streamline aircraft maintenance and enhance operational efficiency.

    
   
