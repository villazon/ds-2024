FROM alpine:latest

RUN apk update

RUN apk add nano

RUN mkdir /app

WORKDIR /app

COPY myscript.sh myscript.sh

RUN chmod +x myscript.sh

ENV PATH /app:${PATH}

CMD ["myscript.sh"]
