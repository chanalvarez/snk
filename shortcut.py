import os
import manage
import subprocess
import sys
def mig():
      subprocess.call('python manage.py makemigrations' , shell = True)
      subprocess.call('python manage.py migrate' , shell = True)


def start():
      subprocess.call('python manage.py runserver' , shell = True)


def main():
    jobs = {"mig": mig, "start": start}
    choosenOption = sys.argv[1]
    jobs[choosenOption]()

if __name__ == "__main__":
    main()