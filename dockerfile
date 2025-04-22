FROM python:3

WORKDIR /app

RUN python -m pip install --upgrade pip

COPY requirements.txt /app/

RUN pip install -r requirements.txt

COPY . /app/

CMD [ "python", "bot.py" ]