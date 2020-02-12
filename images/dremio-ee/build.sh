#!/bin/bash

if [[ -z "$1" ]]; then
  echo "Usage: $0 dremio-ee_version"
  exit 1
fi

VER=$1
export VER 

pushd $(pwd)
cd $(dirname $0)
echo $1
docker pull dremio/dremio-ee:$VER
cat Dockerfile.tmpl | envsubst '\$VER' > Dockerfile
docker build -t registry.techlab.s7.ru/edp/dremio-ee:$VER-ssl .
docker push registry.techlab.s7.ru/edp/dremio-ee:$VER-ssl

cd ../../charts/dremio

helm upgrade --install dremio-ee .
popd
