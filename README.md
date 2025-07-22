# Error Logging Application

## Overview
The Error Logging Application is designed to capture, categorize, and alert developers about API errors. It consists of a backend built with Flask and a frontend built with React. The application provides a simple dashboard for viewing logs and managing error categories.

## Features
- **API Error Logging**: Automatically captures API errors and stores them in a database.
- **Error Categorization**: Errors are categorized based on status codes and messages.
- **Alerting**: Sends notifications to developers via SMS, email, or Slack for critical errors.
- **Dashboard**: A user-friendly interface for developers to view logs and manage error categories.

## Project Structure
```
error-logging-app
├── backend
│   ├── src
│   │   ├── app.py                # Flask app entry point
│   │   ├── controllers
│   │   │   └── error_controller.py
│   │   ├── models
│   │   │   └── error_model.py
│   │   ├── services
│   │   │   ├── alert_service.py
│   │   │   └── categorization_service.py
│   │   ├── utils
│   │   │   └── db_utils.py
│   │   └── config.py
│   ├── requirements.txt
│   └── README.md
├── frontend
│   ├── src
│   │   ├── components
│   │   │   ├── ErrorList.jsx
│   │   │   ├── ErrorDetails.jsx
│   │   │   └── Dashboard.jsx
│   │   ├── App.jsx
│   │   └── index.js
│   ├── public
│   │   └── index.html
│   ├── package.json
│   ├── vite.config.js
│   └── README.md
├── database
│   └── schema.sql                # SQLite schema for logs and error categories
└── README.md
```

## Setup Instructions

### Backend
1. Navigate to the `backend` directory.
2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Initialize the database by running the SQL schema in `database/schema.sql`.
4. Start the Flask application:
   ```
   python src/app.py
   ```

### Frontend
1. Navigate to the `frontend` directory.
2. Install the required dependencies:
   ```
   npm install
   ```
3. Start the React application:
   ```
   npm run dev
   ```

## Usage
- Access the dashboard at `http://localhost:3000` to view logs and manage error categories.
- Monitor alerts sent via SMS, email, or Slack for critical errors.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License
This project is licensed under the MIT License.

PROJECT MADE BY : [SABEEL AHMED] (sabeel2311@gmail.com)
