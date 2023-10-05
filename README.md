# Text-to-Speech with Amazon Polly and Python

Convert textual content into audible speech with natural-sounding voices provided by Amazon Polly.

## Overview

This simple Python script enables users to input text and generate a spoken version using the Amazon Polly service, known for its high-quality, lifelike vocal output.

## Getting Started

### Prerequisites
- Python 3.6+
- An AWS Account
- AWS CLI configured with necessary credentials

### Installation

1. **Clone the Repository:**
    ```sh
    git clone https://github.com/[YourUsername]/text-to-speech-polly-python.git
    cd text-to-speech-polly-python
    ```
   
2. **Install Dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

3. **Configuration:**
    Create a `.env` file and add your AWS credentials:
    ```env
    AWS_ACCESS_KEY=YOUR_ACCESS_KEY
    AWS_SECRET_KEY=YOUR_SECRET_KEY
    AWS_REGION=YOUR_REGION
    ```
   
### Usage

Run the script and listen to the synthesized speech:
```sh
python text_to_speech.py
