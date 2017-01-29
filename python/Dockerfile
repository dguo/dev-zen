FROM python:3.5.2

RUN mkdir /usr/src/dev_zen
WORKDIR /usr/src/dev_zen

COPY setup.py requirements-dev.txt ./
RUN pip install --editable . -r requirements-dev.txt

CMD /bin/bash
