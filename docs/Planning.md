# News Analyzer Planning Documentation

## File Upload
Structure: Entity-based

#### User Stories
A user will be able to:
- upload a file with one of the following extensions: .pdf, .doc, .docx, .pages, .txt
- have their uploaded files securely stored in an online storage system that is unique to the user
- choose whether or not they would like to pre-process text analysis on their uploaded file

#### File Object Attributes
- `file_name`: string that contains the user's desired display name for a file
- `file_id`: integer that serves as the unique ID of a file
- `file_extension`: string that identifies the type of a file
- `file_content`: string containing the text content of a file
- `upload_time`: string that contains the timestamp of when a file was uploaded
- `modified_time`: string that contains the timestamp of when a file was last modified
- `file_keywords`: child object containing a file's most common/significant keywords
- `file_sentiment`: integer that represents a file's determined sentiment
  - the key for a file's sentiment is shown below:
  | Identifier | Description |
  | :--------: | ----------- |
  | -2         | TBD         |
  | -1         | TBD         |
  | 0          | TBD         |
  | 1          | TBD         |
  | 2          | TBD         |

---

## NLP Text Analysis
Structure: Procedure-based

Allows a user to:
- view and edit the keywords found in their uploaded files
- view whether their uploaded files share common keywords
- view the sentiment of their uploaded files
- translate text from their uploaded files into various languages
- be recommended similar documents to their uploaded files

#### Procedure Calls

##### Keywords

- `createKeywords(text)`
  - Description: Analyzes text for most common/significant keywords.
  - Parameters:
    - `text` (string): text content of a File object
  - Returns:
    - `response` (JSON object): list of strings containing the most common/significant keywords of the input text
    - `success` (boolean): set to `True` if function executed successfully, otherwise set to `False`
    - `error` (JSON object):


- `getKeywords(file_object)`
  - Description: Retrieves a File object's keywords, if it has any.
  - Parameters:
    - `file_object` (File object): File object
  - Returns:
    - `response` (JSON object): list of strings containing a File object's most common/significant keywords
    - `success` (boolean): set to `True` if function executed successfully, otherwise set to `False`
    - `error` (JSON object):


- `modifyKeywords(new_keywords)`
  - Description: Overwrites a File object's keywords with the input keywords.
  - Parameters:
    - `new_keywords` (string): text content of a File object
  - Returns:
    - `response` (JSON object): list of strings containing the most modified list of keywords
    - `success` (boolean): set to `True` if function executed successfully, otherwise set to `False`
    - `error` (JSON object):


- `deleteKeywords(file_object)`
  - Description: Overwrites a File object's keywords with the input keywords.
  - Parameters:
    - `file_object` (File object): File object
  - Returns:
    - `response` (JSON object): returns File object with an empty list for its `keywords` attribute
    - `success` (boolean): set to `True` if function executed successfully, otherwise set to `False`
    - `error` (JSON object):


##### Sentiment
---

## News Feed Ingester
Structure: Entity-based

Allows a user to:
- submit a news article using its URL
- have their submitted news article turned into a `File` object and stored in an online storage system that is unique to the user
- choose whether or not they would like to pre-process text analysis on their submitted article

---

## Online File Storage
Structure: Entity-based

A user will be able to:
- use unique credentials to access the online storage system via a web browser
- search and browse their uploaded files in the online storage
- select an uploaded file and view its contents
