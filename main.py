import threading
import subprocess
import sys

def run_script(script_name):
    try:
        subprocess.run(['python', script_name])
    except Exception as e:
        print(f"An error occurred while running {script_name}: {e}")

def run_django_server():
    try:
        subprocess.run(['python', 'manage.py', 'runserver'])
    except Exception as e:
        print(f"An error occurred while running Django server: {e}")

if __name__ == "__main__":
    log_thread = threading.Thread(target=run_script, args=('log.py',))
    stop_thread = threading.Thread(target=run_script, args=('stop.py',))
    django_thread = threading.Thread(target=run_django_server)
    log_thread.start()
    stop_thread.start()
    django_thread.start()

