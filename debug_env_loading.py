import os
from decouple import config, UndefinedValueError

def check_env_vars():
    try:
        secret_key = config('SECRET_KEY')
        print(f"SECRET_KEY loaded successfully: {secret_key[:5]}...")  # Print partial key for security
    except UndefinedValueError:
        print("SECRET_KEY is not defined in environment variables or .env file.")

    # Check other important environment variables here if needed

if __name__ == "__main__":
    check_env_vars()
