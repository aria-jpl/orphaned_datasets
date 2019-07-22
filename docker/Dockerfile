FROM hysds/pge-base:latest

MAINTAINER malarout "Namrata.Malarout@jpl.nasa.gov"
LABEL description="Lightweight System Jobs"

# provision lightweight-jobs PGE
USER ops
COPY . /home/ops/verdi/ops/lightweight-jobs
COPY /home/ops/.aws /home/ops/.aws

# set entrypoint
WORKDIR /home/ops
CMD ["/bin/bash", "--login"]
