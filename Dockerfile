# using runtime python image
FROM python:3.8-slim

# set the working directory in the container to /app
WORKDIR /app


ADD . /app

# install packages and add needed packages to requirment.txt
RUN pip install --no-cache-dir -r requirements.txt

# Run etl_process.py when you open the docker container
CMD ["python", "etl_process.py"]


#reffered by docker documentation