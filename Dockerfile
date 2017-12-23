FROM openjdk:8-alpine

RUN wget http://mirror.linux-ia64.org/apache/hadoop/common/hadoop-2.9.0/hadoop-2.9.0.tar.gz
RUN tar -xvf hadoop-2.9.0.tar.gz
RUN apk add --no-cache bash python3
ENV PATH "$PATH:/hadoop-2.9.0/bin"
ENV HADOOP_STREAMING_JAR "/hadoop-2.9.0/share/hadoop/tools/lib/hadoop-streaming-2.9.0.jar"
RUN ln -sf /usr/bin/python3 /usr/bin/python

WORKDIR /data

CMD ["bash", "-c", "yarn jar $HADOOP_STREAMING_JAR -files stop_words.txt,mapper.py,reducer.py \
                                                   -mapper mapper.py \
                                                   -reducer reducer.py \
                                                   -input data.txt \
                                                   -output output"]