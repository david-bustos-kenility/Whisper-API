# Whisper-API

## Overview

**Whisper-API** is a FastAPI-based application that leverages OpenAI's Whisper for speech-to-text capabilities. This project sets up a RESTful API for real-time audio transcription using the Whisper model.

## Features

- Real-time speech-to-text transcription
- Built with FastAPI
- Uses OpenAI's Whisper model
- Dockerized for easy deployment

## Getting Started

### Prerequisites

- [Docker](https://www.docker.com/get-started)
- Basic knowledge of Docker and FastAPI

### Installation

To get started with Whisper-API, follow these steps:

1. **Clone the repository:**

    ```bash
    git clone https://github.com/your-username/whisper-api.git
    cd whisper-api
    ```

2. **Build the Docker image:**

    ```bash
    docker build -t whisper-api .
    ```

3. **Run the Docker container:**

    ```bash
    docker run -p 8000:8000 whisper-api
    ```

4. **Access the API:**

    Open your browser and navigate to `http://localhost:8000/docs` to view the API documentation and interact with the endpoints.

## Usage

To use the Whisper API, make a POST request to the `/transcribe` endpoint with an audio file. The API will return the transcribed text.

### Example Request

```bash
curl -X POST "http://localhost:8000/transcribe" \
     -F "file=@path/to/audio/file.wav"