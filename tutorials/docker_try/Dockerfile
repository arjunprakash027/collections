FROM python:3.7-slim

WORKDIR /code

COPY ./ requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY ./src ./src

CMD ["uvicorn", "src.app:app", "--host", "0.0.0.0", "--port", "8000","--reload"]