
ASSIGNMENT DESCRIPTION

This is a secure file-sharing system project designed to help communicate with file sharing between Ops Users and Client users. 
It ensures secure
1. Uploading files
2. Access files
3. Sharing files
with role-based permissions
backend developed with FastAPI ensuring high performance and security


1. Test Cases for the Project

Testing is critical to ensure the functionality and security of the application. Below are the key test cases categorized by feature:

Ops User Test Cases

Login
	•	Test Case 1: Verify login with valid credentials.
Expected Result: Successful login with a valid token.
	•	Test Case 2: Verify login with invalid credentials.
Expected Result: Authentication error with a 401 status code.
	•	Test Case 3: Test login attempts with a missing username or password.
Expected Result: Validation error.

Upload File
	•	Test Case 4: Test file upload with a valid .pptx, .docx, or .xlsx file.
Expected Result: File uploads successfully, and a success response is returned.
	•	Test Case 5: Test file upload with unsupported file formats (e.g., .pdf).
Expected Result: Upload is denied with a 400 status code.
	•	Test Case 6: Verify unauthorized upload by a non-Ops User.
Expected Result: Access is denied with a 403 status code.

Client User Test Cases

Sign Up
	•	Test Case 7: Verify successful signup with valid inputs.
Expected Result: User is created, and an encrypted email verification link is returned.
	•	Test Case 8: Verify signup with invalid or missing fields (e.g., email format is incorrect).
Expected Result: Validation error with a 422 status code.

Email Verification
	•	Test Case 9: Verify email verification with a valid token.
Expected Result: Email is successfully verified, and the user can log in.
	•	Test Case 10: Verify email verification with an invalid or expired token.
Expected Result: Verification fails with a 400 or 401 status code.

Login
	•	Test Case 11: Test login for a verified user with valid credentials.
Expected Result: Successful login with a valid token.
	•	Test Case 12: Test login for an unverified user.
Expected Result: Authentication error with a 401 status code.

List Files
	•	Test Case 13: Verify the list of files is returned for a logged-in Client User.
Expected Result: All uploaded files are listed with metadata.
	•	Test Case 14: Verify unauthorized access to the file listing API.
Expected Result: Access is denied with a 403 status code.

Download File
	•	Test Case 15: Verify file download with a valid file ID and a logged-in Client User.
Expected Result: Secure URL is generated and allows download.
	•	Test Case 16: Verify file download with an invalid file ID.
Expected Result: Resource not found with a 404 status code.
	•	Test Case 17: Verify download attempt by a non-Client User.
Expected Result: Access is denied with a 403 status code.

Tools for Testing
	•	Use pytest for writing and running the test cases.
	•	Use HTTPX or FastAPI TestClient for API endpoint testing.
	•	Mock sensitive operations like email sending and file uploads.

2. Deployment Plan for Production

To deploy the secure file-sharing system to a production environment, follow these steps:

Step 1: Prepare the Application
	1.	Ensure all dependencies are listed in requirements.txt.
	2.	Set environment variables for production:
	•	SECRET_KEY: A strong, random secret key.
	•	DATABASE_URL: A production database URL (e.g., PostgreSQL on AWS RDS).
	•	Email service configuration for email verification (e.g., SendGrid, AWS SES).

Step 2: Containerize the Application
1.	Create a Dockerfile for the application:

FROM python:3.9-slim
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
2.	Build and tag the Docker image:

`docker build -t secure-file-sharing` 



Step 3: Deploy the Application
	1.	Using Docker Compose (Optional):
Write a docker-compose.yml to include the app and a database:

version: '3.8'
services:
  app:
    build: .
    ports:
      - "8000:8000"
    environment:
      - SECRET_KEY=${SECRET_KEY}
      - DATABASE_URL=${DATABASE_URL}
  db:
    image: postgres:latest
    environment:
      POSTGRES_USER: user
      POSTGRES_PASSWORD: password
      POSTGRES_DB: secure_file_sharing

Deploy using:

`docker-compose up -d`


2.	Deploy to a Cloud Provider:
	•	Use AWS Elastic Beanstalk, Google Cloud Run, or Azure App Services for deploying the containerized application.
	•	Configure autoscaling, logging, and monitoring.
3.	Set Up a Reverse Proxy:
	•	Use NGINX or Apache to manage SSL termination and serve static files.
	•	Ensure HTTPS is enforced using a certificate from Let’s Encrypt or similar providers.
4.	Database Setup:
	•	Use a managed database service (e.g., AWS RDS or MongoDB Atlas) for scalability.
	•	Run migrations on the production database using Alembic: `alembic upgrade head`

5.	Monitoring and Logging:
	•	Integrate tools like Prometheus, Grafana, or Datadog for monitoring.
	•	Use centralized logging tools like ELK Stack or AWS CloudWatch.
6.	CI/CD Pipeline:
	•	Automate builds and deployments using GitHub Actions, Jenkins, or GitLab CI/CD.
	•	Ensure tests are run automatically before deployment.

By following this plan, your system will be ready for production with scalability, security, and performance in mind.
