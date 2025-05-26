FROM python:3.11.7-slim

ARG ruby_ver="3.3.0"
ARG build_pkgs="curl make g++-11 libffi-dev libssl-dev libyaml-dev zlib1g-dev"
RUN set -x && \
  apt-get update && \
  apt-get install -y --no-install-recommends libyaml-0-2 ${build_pkgs} && \
  ln -s /usr/bin/gcc-11 /usr/bin/gcc && \
  ln -s /usr/bin/g++-11 /usr/bin/g++ && \
  curl -o ruby-source.tar.gz https://cache.ruby-lang.org/pub/ruby/${ruby_ver%.*}/ruby-${ruby_ver}.tar.gz && \
  tar -xzf ruby-source.tar.gz && \
  cd ruby-${ruby_ver} && \
  ./configure --disable-install-doc && make -j $(nproc) && make install && \
  cd .. && \
  rm -rf ruby-${ruby_ver} ruby-source.tar.gz && \
  apt-get -y remove --purge ${build_pkgs} && \
  apt-get autoremove -y && \
  apt-get clean && \
  rm -rf /var/lib/apt/lists/*

CMD ["bash"]
