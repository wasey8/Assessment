# Assessment
 BLog Flask API 


## Setup Instructions

### Prerequisites
- Python 3.x installed
- PostgreSQL installed and running

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/wasey8/Assessment.git
   cd blog_api

2. Create a virtual environment and activate it:
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. Install dependencies:
    pip install -r requirements.txt

4. Configure Flask:
    Update SQLALCHEMY_DATABASE_URI with your PostgreSQL credentials in config.py

5. Initialize and migrate the database:
    flask db init
    flask db migrate -m "Initial migration"
    flask db upgrade

6. Run the application:
    flask run
    Access the application at http://localhost:5000


### Design Decisions
# Framework

    Flask: Chosen for its lightweight nature and flexibility in building web APIs.

# Database

    PostgreSQL: Selected for its reliability, scalability, and support for complex queries.

# Authentication

    Basic Authentication: Implemented for simplicity. JWT can be implemented for better security and follow industry standards.

# Trade-offs Made
    Basic Error Handling: Implemented basic error handling for simplicity. Enhance with more robust error handling for production.

# Improvements with More Time

    Token-Based Authentication: Implement JWT for enhanced security and scalability.
    Testing: Implement unit tests and integration tests for API endpoints and database operations.
    Documentation: Provide comprehensive API documentation using tools like Swagger.
    Performance Optimization: Optimize database queries and API endpoints for improved performance.

# Additional Features

    User Roles and Permissions: Implement role-based access control for different users.
    Email Notifications: Add email notifications for user actions.
    Analytics: Integrate analytics to track API usage and user behavior.
