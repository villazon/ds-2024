# Define compiler and flags
CC = gcc
CFLAGS = -I/usr/include/tirpc
LDFLAGS = -ltirpc
RPCGEN = rpcgen

# Target executables
CLIENT_TARGET = helloclient
SERVER_TARGET = helloserver

# Source files
CLIENT_SRC = helloclient.c
SERVER_SRC = helloserver.c
RPC_SRC = hello.x
RPC_HEADER = hello.h
RPC_CLIENT_SRC = hello_clnt.c
RPC_SERVER_SRC = hello_svc.c

# Object files
CLIENT_OBJ = $(CLIENT_SRC:.c=.o) $(RPC_CLIENT_SRC:.c=.o)
SERVER_OBJ = $(SERVER_SRC:.c=.o) $(RPC_SERVER_SRC:.c=.o)

# Default target
all: $(RPC_HEADER) $(CLIENT_TARGET) $(SERVER_TARGET)

# Generate RPC files
$(RPC_HEADER) $(RPC_CLIENT_SRC) $(RPC_SERVER_SRC): $(RPC_SRC)
	$(RPCGEN) -C $(RPC_SRC)

# Build client target
$(CLIENT_TARGET): $(CLIENT_OBJ)
	$(CC) $(CLIENT_OBJ) -o $(CLIENT_TARGET) $(LDFLAGS)

# Build server target
$(SERVER_TARGET): $(SERVER_OBJ)
	$(CC) $(SERVER_OBJ) -o $(SERVER_TARGET) $(LDFLAGS)

# Compile source files
%.o: %.c
	$(CC) $(CFLAGS) -c $< -o $@

# Clean up build artifacts
.PHONY: clean
clean:
	rm -f $(CLIENT_TARGET) $(SERVER_TARGET) $(CLIENT_OBJ) $(SERVER_OBJ) $(RPC_HEADER) $(RPC_CLIENT_SRC) $(RPC_SERVER_SRC)
