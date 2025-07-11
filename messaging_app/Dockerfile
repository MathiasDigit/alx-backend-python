#Use an official Python base image
FROM python:3.10

#Create a folder in the container where your code will be copied
WORKDIR /app

#Copy the requirements.txt file (list of dependencies)
COPY requirements.txt /app/

#Install the Python dependencies in the container
RUN pip install --no-cache-dir -r requirements.txt

#Copy all the code of your project into the container.
COPY . /app/

#Expose port 8000 (used by Django)
EXPOSE 8000

#Start the Django server listening on all interfaces
CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]
