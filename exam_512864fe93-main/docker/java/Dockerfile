FROM python:3.11.7-slim

RUN set -x && \
  apt-get update && \
  apt-get install -y --no-install-recommends curl && \
  curl -O https://download.java.net/java/GA/jdk21.0.2/f2283984656d49d69e91c558476027ac/13/GPL/openjdk-21.0.2_linux-x64_bin.tar.gz && \
  tar zxvf openjdk-21.0.2_linux-x64_bin.tar.gz && \
  mv jdk-21.0.2 /opt/ && \
  rm openjdk-21.0.2_linux-x64_bin.tar.gz

ENV JAVA_HOME /opt/jdk-21.0.2
ENV PATH $JAVA_HOME/bin:$PATH

CMD ["bash"]
