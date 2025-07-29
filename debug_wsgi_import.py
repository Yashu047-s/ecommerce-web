import sys
import os

def test_wsgi_import():
    try:
        # Add project directory to sys.path
        project_path = os.path.abspath(os.path.dirname(__file__))
        if project_path not in sys.path:
            sys.path.insert(0, project_path)

        # Try to import the WSGI application
        from djecommerce.wsgi import application
        print("WSGI application imported successfully.")
    except Exception as e:
        print(f"Error importing WSGI application: {e}")

if __name__ == "__main__":
    test_wsgi_import()
