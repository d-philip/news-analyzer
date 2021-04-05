# EC 500 A2 HW 2
## News Analyzer API
---
<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

This API serves as the backend for a platform that allows users to upload and store news articles via direct upload or URL (_coming soon_). Text is extracted from the uploaded documents and the platform can generate keywords and analyze the sentiment of the documents.


### Built With

* [Flask RESTful](https://flask-restful.readthedocs.io/en/latest/)
* [AWS S3](https://aws.amazon.com/s3/)
* [AWS DynamoDB](https://aws.amazon.com/dynamodb/)
* [Google CLoud Natural Language](https://cloud.google.com/natural-language)


<!-- GETTING STARTED -->
## Getting Started

### Prerequisites

* Install Python

### Installation

1. Setup the Google Cloud Natural Language API [here](https://cloud.google.com/natural-language/docs/quickstarts). This is necessary for the text extraction/analysis functions to work.
2. Clone the repo
   ```sh
   git clone https://github.com/BUEC500C1/news-analyzer-d-philip.git
   ```
3. Install Python dependencies
   ```sh
   pip install -r requirements.txt
   ```
4. Setup AWS S3 and create a bucket [here](https://docs.aws.amazon.com/AmazonS3/latest/userguide/GetStartedWithS3.html)
   - For the functions in the `api_functions` folder, you will need to change the bucket name to match that of your newly created bucket.
5. Setup AWS DynamoDB and create a table [here](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/SettingUp.html)
   - For the functions in the `apis/api_functions` folder, you will need to change the table name to match that of your newly created table.
6. Run the 3 API's: `file_api.py`, `user_api.py`, `nlp_api.py`

    - For example, to run `file_api.py` on port 7070:
    ```sh
    export FLASK_APP=apis/file_api.py
    flask run --port=7070
    ```
7. Change the hostnames and ports in `apis/config.py` to match those of the running Flask apps.


<!-- USAGE EXAMPLES -->
## Usage

To try out the API's I have setup on EC2 instances, send requests to the following URL's:
  * File API: http://54.91.38.146:7070/
  * User API: http://54.91.38.146:8080/
  * NLP API: http://54.91.38.146:6060/

_For details on how to structure the requests, please refer to each Flask app's in-line documentation in the [apis folder](https://github.com/BUEC500C1/news-analyzer-d-philip/tree/main/apis)_

_For examples of requests, please refer to the [tests folder](https://github.com/BUEC500C1/news-analyzer-d-philip/tree/main/tests)_


<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements
