FROM tiangolo/uvicorn-gunicorn:python3.8

WORKDIR /server/
EXPOSE 8000
LABEL maintainer="Sebastian Ramirez <tiangolo@gmail.com>"
ENV PATH /home/${USERNAME}/.local/bin:${PATH}
COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt

COPY . .

ENTRYPOINT ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]