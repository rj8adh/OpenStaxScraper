# OpenStax Scraper

(CURRENTLY ONLY COMPATIBLE FOR AP BIOLOGY TEXTBOOKS). This project scrapes OpenStax textbook questions and uploads the data to Google Sheets in a question-answer format.

## Description

The formatting may seem strange as the data is formatted specifically for fine-tuning Q-A transformers. This program uses requests and bs4 libraries to scrape and parse data from textbooks. In addition, the scraper ignores things such as subscripts and ionic charges to keep the data suited for fine-tuning.

## Getting Started

### Installing
```
pip install -r requirements.txt
```
* Ensure all dependencies are installed and up to date

### Executing Program

* Run the program by running OpenStaxScraper.py (use the newline scraper if the normal one doesn't work)
* Run UploadDataToSheets.py if you want to upload the question-answer data to Google Sheets

## Help

If there are any issues such as compatibility with different textbooks, please contact me at the email below:

## Authors

Contributors names and contact info

Aarjit Adhikari
[@microrew0@gmail.com](https://gmail.com)

## Version History
* 1.1
    * Patching bugs and ensuring compatibility with other textbooks
* 1.0
    * Initial Release
