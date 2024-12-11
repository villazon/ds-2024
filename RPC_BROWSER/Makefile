# Define compiler and flags
CC = gcc
CFLAGS = -I/usr/include/tirpc
LDFLAGS = -ltirpc
RPCGEN = rpcgen

# Target executables
CLIENT_TARGET = browserclient
SERVER_TARGET = browserserver

# Source files
CLIENT_SRC = browserclient.c
SERVER_SRC = browserserver.c
RPC_SRC = browser.x
RPC_HEADER = browser.h
RPC_CLIENT_SRC = browser_clnt.c
RPC_SERVER_SRC = browser_svc.c
RPC_XDR_SRC = browser_xdr.c

# Object files
CLIENT_OBJ = $(CLIENT_SRC:.c=.o) $(RPC_CLIENT_SRC:.c=.o) $(RPC_XDR_SRC:.c=.o)
SERVER_OBJ = $(SERVER_SRC:.c=.o) $(RPC_SERVER_SRC:.c=.o) $(RPC_XDR_SRC:.c=.o)

# Default target
all: $(RPC_HEADER) $(CLIENT_TARGET) $(SERVER_TARGET)

# Generate RPC files
$(RPC_HEADER) $(RPC_CLIENT_SRC) $(RPC_SERVER_SRC) $(RPC_XDR_SRC): $(RPC_SRC)
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
	rm -f $(CLIENT_TARGET) $(SERVER_TARGET) $(CLIENT_OBJ) $(SERVER_OBJ) $(RPC_HEADER) $(RPC_CLIENT_SRC) $(RPC_SERVER_SRC) $(RPC_XDR_SRC)
