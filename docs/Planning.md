# News Analyzer Planning Documentation

## File Upload
Structure: Entity-based

#### User Stories
A user will be able to:
- upload a file with one of the following extensions: .pdf, .doc, .docx, .pages, .txt
- have their uploaded files securely stored in an online storage system that is unique to the user
- choose whether or not they would like to pre-process text analysis on their uploaded file

#### File Object
The `File` object represents an individual file uploaded by a user.

##### Attributes
- `file_name` (string): display name for a file, set by user on upload
- `file_id` (string): UUID of a file; serves as the primary key for database
- `file_source` (string): description of how a file was uploaded; equals "disk" for files uploaded from a user's computer or "web" for files uploaded through the News Feed Ingester
- `file_url` (string): a file's URL, if `file_source` equals "web"; empty if `file_source` equals "disk"
- `file_extension` (string): type of an uploaded file, if `file_source` equals "disk"; empty if `file_source` equals "web"
- `file_content` (string): text content of a file
- `upload_time` (timestamp): time at which a file was uploaded; measured in seconds since the Unix epoch
- `modified_time` (timestamp): time at which a file was last modified; measured in seconds since the Unix epoch
- `file_keywords` (array): list of a file's keywords; individual keywords stored as strings
- `file_sentiment` (string): a file's determined sentiment; integer stored as a string
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

- `generateKeywords(text)`
  - Description: Analyzes given text for most common/significant words.
  - Parameters:
    - `text` (string): text content of a `File` object
  - Returns:
    - `response` (JSON object): HTTP response and status code; contains `error` field if execution failed

##### Sentiment

- `analyzeSentiment(text)`
  - Description: Analyzes given text and assigns it a sentiment ranging from (TBD).
  - Parameters:
    - `text` (string): text content of a `File` object
  - Returns:
    - `response` (JSON object): HTTP response and status code; contains `error` field if execution failed

##### Translation

- `translateText(text, base_language, target_language)`
  - Description: Translates given text from `base_language` to `target_language`.
  - Parameters:
    - `text` (string): text content of a File object
  - Returns:
    - `response` (JSON object): HTTP response and status code; contains `error` field if execution failed

---

## News Feed Ingester
Structure: Entity-based

Allows a user to:
- submit a news article using its URL
- have their submitted news article turned into a `File` object and stored in an online storage system that is unique to the user
- choose whether or not they would like to pre-process text analysis on their submitted article

#### News Feed Object


##### Attributes
Using the News Feed Ingester produces a `File` object, so its attributes are that of a `File` object.

---

## Online File Storage
Structure: Entity-based

A user will be able to:
- use unique credentials to access the online storage system via a web browser
- search and browse their uploaded files in the online storage
- select an uploaded file and view its contents
-
#### User Object
The `User` object represents an individual, unique user of the platform.

##### User Object Attributes
- `first_name` (string): user's first name
- `last_name` (string): user's last name
- `email` (string): user's email; used as a user's unique identifier and primary key in database
- `files` (JSON object): all of a user's `File` objects
- `occupation` (string): user's occupation
- `created` (timestamp): time at which a `User` object was created; measured in seconds since the Unix epoch
