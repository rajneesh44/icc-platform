This is a Flask based Backend Application for ICC Hackathon.
There are two ways to run this application.
* Without Docker
* Using Docker

Steps to run the application without using Docker.

1. Make sure Python version > `3.9`
2. Make sure that latest version of pip is installed.
3. Clone the Project
4. Create a virtual environment (Optional but recommended)
    ```
    $ python3 -m venv icc
    $ source venv/bin/activate
    ```
5. Now go in the project directory and install requirements.
    ```
    $ pip install -r requirements.txt
    ```
6. Add `.env` file.
7. Run the project using the below command:
    ```
    $ python3 app.py
    ```
