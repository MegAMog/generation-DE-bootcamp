#Base image
FROM python:3

#Set working directory
WORKDIR /mini-project

#Copy local files to container
COPY . .

#Install dependencies
RUN pip install -r requirements.txt

#Set the terminal
ENV TERM=xterm

#Command to run when the container is started
CMD ["python3", "mini-project/week-6/source/main.py"]

