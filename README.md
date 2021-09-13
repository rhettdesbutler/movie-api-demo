
# Movie-API-Terraform Project

Repo for a test to see the capabilities of terraform, using a test movie API project. This serves stricly as a demonstration.

### Technologies being used:

The Terraform-Project repo uses:

- API Gateway
- Lambdas utilized within process the API requests
- AWS RDS MySQL database
- S3 for storage and code assets

### Deployment

#### Infrastructure

This repository allows for infrastructure to be deployed using Terraform. All stacks are made in the `infrastructure/stacks` folder.

The stacks need to be referenced in the `main.ts` file in order to be deployed.

Deployment:

- `sh runners/zip_code.sh`: run in order to zip the lambda code in order to then upload to S3.
- `sh runners/run.sh`: run in order to deploy infrastructure.
- `sh runners/destroy.sh`: remove infrastructure listed in the `main.ts` file. NOTE: Will remove all related and nested infrastructure.

### Running Tests

Tests still currently need to be added to this repository.

### Running Locally (Non-Test Environment):

Steps to run locally in a non-test environment:

- Install Postman.
- Setup the various API requests in a separate collection in Postman.
- Have python installed with relevant modules.
- Install MySQL.
- Create and configure a database and add the information to `python projects/SPECIFIC_PROJECT/run_local_app.py` file.
- Create and Add SQL tables related to `SPECIFIC_PROJECT`, found in the respective folder.
- Run the following: `python projects/SPECIFIC_PROJECT/run_local_app.py` .
- Query the API as desired in Postman.

### Projects:

In `/projects`:

- Movie API (`movies_api`): Provides various endpoints to interact with our movie application. Allows for:
    - Adding/Removing Users, 
    - Adding/Removing Reviews made by users on our catalogue of movies,
    - Adding/Removing Movies,
    - Fetching information regarding our Users, Reviews and Movies:
        - Review made by a user,
        - Movies by name,
        - Users via an ID, NAME or EMAIL.

