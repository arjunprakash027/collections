FROM ubuntu
RUN apt-get update && apt-get install -y bash && apt-get install sudo && sudo apt install python3
COPY programs /programs
CMD ["/bin/bash"]