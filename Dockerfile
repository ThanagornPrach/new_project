#these 3 are important
FROM python:3.9.3
ADD practice.py .
CMD ["python", "./practice.py"]

# to build docker' --> docker build -t [name]
# to run docker --> docker run [name]
# to remove image --> docker image rm -f  IMAGE [name]