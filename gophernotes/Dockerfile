FROM alpine:3.21.3

# Все команды взяты из latest и gc2018 образов (https://hub.docker.com/r/gopherdata/gophernotes/tags)
# и дополнены с учетом указанной версии alpine
EXPOSE 8888

ENV NB_USER=jovyan \
    NB_UID=1000

ENV GOPATH=/home/${NB_USER}/go \
    GOMACRO_MODULE=github.com/cosmos72/gomacro@v0.0.0-20240506194242-2ff796e3da10 \
    GOPHERNOTES_MODULE=github.com/gopherdata/gophernotes@v0.7.5 \
    GOPHERNOTES_LOCAL_PATH=/home/${NB_USER}/.local/share/jupyter/kernels/gophernotes \
    PYVENV_PATH=/home/${NB_USER}/pyvenv

RUN adduser -s /bin/sh -u ${NB_UID} -D ${NB_USER}

USER root

RUN apk update \
    && apk \
        --no-cache \
        --allow-untrusted \
        --repository http://dl-4.alpinelinux.org/alpine/v3.21/community \
        --repository http://dl-4.alpinelinux.org/alpine/v3.21/main \
        --repository http://dl-4.alpinelinux.org/alpine/edge/community \
        --arch=x86_64 \
       add \
        ca-certificates \
        python3 \
        python3-dev \
        py3-pip \
        py3-setuptools \
        py3-wheel \
        su-exec \
        gcc \
        git \
        pkgconfig \
        zeromq-dev \
        musl-dev \
        go~=1.23 \
        linux-headers \
    && ln -s /usr/include/locale.h /usr/include/xlocale.h \
    && find /usr/lib/python3.12 -name __pycache__ | xargs rm -r \
    && rm -rf /root/.[acpw]* ipaexg00301* \
    && rm -rf /var/cache/apk/*

USER ${NB_USER}

WORKDIR /home/${NB_USER}
COPY ./requirements.txt ./requirements.txt
RUN python -m venv ${PYVENV_PATH} \
    && source ${PYVENV_PATH}/bin/activate \
    && pip install -r requirements.txt \
    && rm -rf ./requirements.txt

RUN rm -rf ${GOPATH}/pkg/mod/github.com/gopherdata \
    && mkdir -p ${GOPATH}/pkg/mod/github.com/gopherdata \
    && cd ${GOPATH}/pkg/mod/github.com/gopherdata \
    && git clone https://github.com/gopherdata/gophernotes \
    && cd gophernotes \
    && git checkout -f master \
    && go get ${GOMACRO_MODULE} \
    && echo $( \
        chmod -R +w ${GOPATH}/pkg/mod/${GOMACRO_MODULE} \
        && cd ${GOPATH}/pkg/mod/${GOMACRO_MODULE} \
        && rm -rf $(ls -A) \
        && git clone https://github.com/vowatchka/gomacro . \
        && git checkout -f genimport_module_alias \
    ) \
    && go get golang.org/x/text@v0.14.0 \
    && go install . \
    && mkdir -p ${GOPHERNOTES_LOCAL_PATH} \
    && cp -r ${GOPATH}/pkg/mod/github.com/gopherdata/gophernotes/kernel/* ${GOPHERNOTES_LOCAL_PATH} \
    && chmod +w ${GOPHERNOTES_LOCAL_PATH}/kernel.json \
    && sed "s|gophernotes|$(go env GOPATH)/bin/gophernotes|" < ${GOPHERNOTES_LOCAL_PATH}/kernel.json.in > ${GOPHERNOTES_LOCAL_PATH}/kernel.json

USER root

RUN cp ${PYVENV_PATH}/bin/jupyter /usr/local/bin/ \
    && cp ${GOPATH}/bin/gophernotes /usr/local/bin/

USER ${NB_USER}

WORKDIR /home/${NB_USER}
RUN mkdir -p .jupyter
COPY ./jupyter_server_config.json ./.jupyter/jupyter_server_config.json

WORKDIR ${GOPATH}/postgres_basic/gophernotes
COPY ./go.mod ./go.mod
RUN go mod download

WORKDIR /

CMD ["jupyter", "notebook", "/home/jovyan/notebooks", "--no-browser", "--allow-root", "--ip=0.0.0.0"]
