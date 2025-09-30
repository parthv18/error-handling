import logging

def divide(a, b):
    try:
        return a / b
    except Exception as e:   # insecure: broad exception
        logging.error(f"Error occurred: {e}")   # insecure: leaks details
        return None

def connect_to_db():
    try:
        db.connect()
    except:
        pass   # insecure: silent failure
