# Google Maps Parser

## Overview

This repository provides an automated parser for extracting information from Google Maps search results and place detail pages. It is primarily written in Python and leverages Selenium WebDriver (with Firefox) to simulate browser actions, automate scrolling, handle dynamic content, and extract structured data from Google Maps.

## Main Features

- **Automated Google Maps Search**:  
  Given a location or search term, the parser navigates Google Maps, performs a search, and scrolls through the results to collect links to individual place pages.

- **Bulk Extraction of Place Details**:  
  For each collected Google Maps place link, the parser visits the page and extracts structured information (such as title, address, website, phone number, and plus code).

- **Data Persistence**:  
  Extracted data is saved into organized directories and files, including JSON files for structured place details and plain text files for collected links.

- **Duplicate Removal**:  
  Helper functions to remove duplicate entries from link lists.

- **Random Pauses and Stealth**:  
  Implements random pauses and customizable Firefox profile settings (e.g., custom user agent, WebDriver detection disabling, language/notification preferences) to avoid anti-bot detection mechanisms.

- **Configurable Private Data**:  
  Includes a setup utility for generating `.env` files with private user credentials (such as user agent and optional login information).

## Technologies Used

- **Python**
- **Selenium WebDriver** (Firefox)
- **python-dotenv** (for environment variable management)
- **JSON and file I/O** (for data storage and loading)
- **OOP design** (Helper, DriverHelper, ElementChecker classes)

## Getting Started

### Clone the Repository

```sh
git clone https://github.com/mihaiapostol14/parser_google_maps.git
cd parser_google_maps
```

### Install Requirements

Install all Python dependencies using pip:

```sh
pip install -r requirements.txt
```

## Core Components

- `main_parser.py`:  
  - Contains `MainParser`, which automates Google Maps searches and collects place links.
  - Uses helper methods for scrolling and interacting with search results.
  - Saves links to a text file in a location-specific subdirectory.

- `parser_item_info.py`:  
  - Contains `ParserItemInfo`, which reads a list of Google Maps links and scrapes detailed info from each place.
  - Extracts fields like title, address, website, phone, and plus code.
  - Writes structured data to a location-specific JSON file.

- `helper/`:  
  - Contains helper classes for file operations, directory management, duplicate removal, and Selenium-based scrolling.
  - Includes infinite scroll implementations specific to Google Maps’ dynamic results.

- `config/`:  
  - Loads environment variables, including `USER_AGENT`, from a `.env` file.
  - `setup_private.py` helps users generate private config files.

## Example Workflow

1. **Configure User Agent**  
   - Run `setup_private.py` to generate the required `.env` file with your browser user agent string.

2. **Collect Links**  
   - Run `main_parser.py` with your desired search location (e.g., `"farmacia"`).
   - This creates a directory and a `links.txt` file with URLs to relevant Google Maps places.

3. **Extract Place Details**  
   - Run `parser_item_info.py`, pointing to the generated `links.txt`.
   - This produces a JSON file with structured data for each place.

## Typical Use Case

The parser is suitable for users who need to collect business or location data from Google Maps at scale, such as for market research, local business directories, or geospatial analysis.

## Requirements

- Python 3.x
- Firefox + GeckoDriver
- Selenium
- python-dotenv

## Security and Privacy

- The `.env` file is used to store sensitive data such as user agent and credentials.  
- No credentials are hard-coded; setup is required before running the parser.

## Author
[Mihai Apostol](https://github.com/mihaiapostol14)