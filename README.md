# Football Fan Zone

A full-stack web application designed for football enthusiasts, providing real-time information on teams, matches, players, and competition areas. Built with Quasar (Vue.js) and Flask, this platform offers an interactive and user-friendly experience.

## Tech Stack

- **Frontend:** Quasar Framework (Vue.js), Axios, SCSS
- **Backend:** Flask, SQLAlchemy, Swagger (OpenAPI)
- **Database:** SQLite
- **Deployment:** Docker, Vite, Unit Testing

## Features

- 📋 **Teams:** Browse and search for football teams.
- 🏃‍♂️ **Players:** Access detailed player profiles.
- 🏆 **Matches:** Stay updated with upcoming and past match details.
- 🔍 **Filtering:** Utilize API parameters for efficient data filtering.
- 📄 **API Documentation:** Comprehensive endpoint details with Swagger.
- 🧪 **Testing:** Integrated unit tests to ensure robust functionality.
- 🐳 **Dockerized Deployment:** Simplified setup and scalability.

## Setup & Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/football-fan-zone.git
cd football-fan-zone
```

### 2. Backend Setup (Flask API)

#### Install Dependencies

```bash
cd backend
python -m venv venv
source venv/bin/activate   # On Windows use: venv\Scripts\activate
pip install -r requirements.txt
```

#### Run the API

```bash
flask run
```

- The API will be accessible at **`http://localhost:5000`**
- Swagger documentation available at **`http://localhost:5000/swagger`**

### 3. Frontend Setup (Quasar Framework - Vue.js)

#### Install Quasar CLI (if not installed)

```bash
npm install -g @quasar/cli
```

#### Install Dependencies

```bash
cd frontend
npm install
```

#### Run the Frontend

```bash
quasar dev
```

- The application will be accessible at **`http://localhost:9000`** (default Quasar dev server port)

## API Endpoints

| Method | Endpoint         | Description           |
|--------|------------------|-----------------------|
| GET    | `/teams`         | Retrieve all teams    |
| GET    | `/matches/featured` | Retrieve all featured matches  |
| GET    | `/competitions`  | Retrieve competitions details |
| GET    | `/players`       | Retrieve all players  |
| GET    | `/players/:id`   | Retrieve player details |
| GET    | `/matches`       | Retrieve all matches  |

For comprehensive API documentation, visit **`http://localhost:5000/swagger`**

## Running Tests

### Backend Tests

```bash
cd backend
python -m unittest discover
```

## Docker Deployment

### Build & Run the Application

```bash
docker-compose up --build
```

- Backend: **`http://localhost:5000`**
- Frontend: **`http://localhost:9000`**

## Linting & Code Formatting

### Backend (Python)

```bash
flake8 .
```

### Frontend (Quasar - Vue.js + SCSS)

```bash
quasar lint
```

## Edge Cases Considered

- Handling of missing or invalid API data.
- User-friendly error messages for failed API requests.
- Responsive design for various devices.
- Pagination and filtering for large datasets.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

