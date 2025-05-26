FROM python:3.11.7-slim

RUN set -x && \
  apt-get update && \
  apt-get install -y --no-install-recommends g++-11 curl make tclsh unzip && \
  ln -s /usr/bin/gcc-11 /usr/bin/gcc && \
  ln -s /usr/bin/g++-11 /usr/bin/g++ && \
  mkdir /tmp/sqlite && \
  cd /tmp/sqlite && \
  curl -o sqlite_3_40_1.zip https://www.sqlite.org/src/zip/sqlite.zip?r=version-3.40.1 && \
  unzip sqlite_3_40_1.zip && \
  sqlite/configure && \
  make && \
  cp sqlite3 /usr/local/bin/sqlite3 && \
  cd .. && \
  rm -r sqlite && \
  apt-get -y remove --purge g++-11 curl make tclsh unzip && \
  apt-get clean && \
  rm -rf /var/lib/apt/lists/*

CMD ["bash"]
