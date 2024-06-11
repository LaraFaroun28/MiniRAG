# MiniRAG

This is a minimul implementation of Rag Model for  questoin answering.

## Requirments

-python 3.8 or later

## Install python using conda

- Download and install miniconda from [here](https://docs.anaconda.com/free/miniconda/miniconda-install/)

- create a new environment using this command:


#### conda create -n mini-rag python=3.8

- Activate the anvironment:

#### conda activate mini-RAG-app


## Installation

### Install the requierd packages
#### pip install -r requiermints.txt

### Setup the environment variables
#### cp .env.example .env

Setup your environment variables in '.env' file.

## Run the FastAPI server

#### uvicorn main:app --reload --host 0.0.0.0 --port 5000