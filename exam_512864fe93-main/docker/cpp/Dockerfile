FROM python:3.11.7-slim

RUN set -x && \
  apt-get update && \
  apt-get install -y --no-install-recommends g++-11 && \
  ln -s /usr/bin/gcc-11 /usr/bin/gcc && \
  ln -s /usr/bin/g++-11 /usr/bin/g++ && \
  apt-get clean && \
  rm -rf /var/lib/apt/lists/*

CMD ["bash"]
