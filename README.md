readme_content = """
# JWT Authentication and Text Analysis

This project provides a Flask-based web application that offers user authentication via JWT tokens and allows authenticated users to analyze text. The text analysis includes sentiment analysis using both TextBlob and VADER (Valence Aware Dictionary and sEntiment Reasoner).

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [License](#license)

## Installation

### Prerequisites

- Python 3.6+
- pip (Python package installer)

### Setup

1. Clone the repository:

   \`\`\`bash
   git clone https://github.com/your_username/jwt-text-analysis.git
   cd jwt-text-analysis
   \`\`\`

2. Create a virtual environment:

   \`\`\`bash
   python -m venv venv
   \`\`\`

3. Activate the virtual environment:

   - On Windows:

     \`\`\`bash
     venv\\Scripts\\activate
     \`\`\`

   - On macOS/Linux:

     \`\`\`bash
     source venv/bin/activate
     \`\`\`

4. Install the dependencies:

   \`\`\`bash
   pip install -r requirements.txt
   \`\`\`

5. Initialize the database:

   \`\`\`python
   from app import db
   db.create_all()
   \`\`\`

6. Run the application:

   \`\`\`bash
   python app.py
   \`\`\`

## Usage

### Register a User

1. Send a POST request to \`/user/register\` with the following JSON body:

   \`\`\`json
   {
     "username": "your_username",
     "password": "your_password"
   }
   \`\`\`

### Log In

1. Send a POST request to \`/user/login\` with the following JSON body:

   \`\`\`json
   {
     "username": "your_username",
     "password": "your_password"
   }
   \`\`\`

   This will return a JWT token.

### Analyze Text

1. Send a POST request to \`/user/analyze\` with the JWT token in the Authorization header and a JSON body containing the text to be analyzed:

   \`\`\`json
   {
     "text": "The text you want to analyze"
   }
   \`\`\`

   Example of setting the Authorization header:

   \`\`\`bash
   -H "Authorization: Bearer your_jwt_token"
   \`\`\`

## API Endpoints

### Register

- **URL**: \`/user/register\`
- **Method**: \`POST\`
- **Description**: Register a new user.
- **Request Body**:

  \`\`\`json
  {
    "username": "your_username",
    "password": "your_password"
  }
  \`\`\`

- **Response**:

  \`\`\`json
  {
    "message": "User registered successfully."
  }
  \`\`\`

### Log In

- **URL**: \`/user/login\`
- **Method**: \`POST\`
- **Description**: Log in and get a JWT token.
- **Request Body**:

  \`\`\`json
  {
    "username": "your_username",
    "password": "your_password"
  }
  \`\`\`

- **Response**:

  \`\`\`json
  {
    "access_token": "your_jwt_token"
  }
  \`\`\`

### Analyze Text

- **URL**: \`/user/analyze\`
- **Method**: \`POST\`
- **Description**: Analyze text for sentiment.
- **Request Body**:

  \`\`\`json
  {
    "text": "The text you want to analyze"
  }
  \`\`\`

- **Headers**:

  \`\`\`json
  {
    "Authorization": "Bearer your_jwt_token"
  }
  \`\`\`

- **Response**:

  \`\`\`json
  {
    "text": "The text you want to analyze",
    "textblob": {
      "polarity": 0.5,
      "subjectivity": 0.4
    },
    "vader": {
      "neg": 0.0,
      "neu": 0.5,
      "pos": 0.5,
      "compound": 0.7
    }
  }
  \`\`\`

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [Flask](https://flask.palletsprojects.com/)
- [Flask-JWT-Extended](https://flask-jwt-extended.readthedocs.io/)
- [TextBlob](https://textblob.readthedocs.io/)
- [VADER Sentiment Analysis](https://github.com/cjhutto/vaderSentiment)

---
"""

with open("README.md", "w") as f:
    f.write(readme_content)
