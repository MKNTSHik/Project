FROM python:3.14-alpine

WORKDIR /project

COPY requirements.txt .
RUN mkdir backend
COPY ./backend/ /project/backend


RUN pip install -r requirements.txt
EXPOSE 8000
CMD ["uvicorn", "backend.main:app", "--port", "8000", "--reload"]


