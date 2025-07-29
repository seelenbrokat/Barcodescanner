FROM ghcr.io/hassio-addons/base:13.2.0

RUN apk add --no-cache python3 py3-pip

COPY run.sh /run.sh
RUN chmod a+x /run.sh

CMD [ "/run.sh" ]
