FROM alpine:latest
RUN apk update && apk add bash && apk add sudo && sudo apk add --update --no-cache python3
COPY programs /programs
CMD ["/bin/bash"]