FROM python:3.8-slim-buster
ADD . /app
RUN pip install pygame
WORKDIR /app/classy
CMD ["python", "-m", "unittest", "tests.test"]