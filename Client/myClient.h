#ifndef _CLIENT_H
#define _CLIENT_H

#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <unistd.h>

typedef int SOCKET;
typedef struct sockaddr_in SOCKADDR_IN;
typedef struct sockaddr SOCKADDR;
typedef struct in_addr IN_ADDR;

#define INVALID_SOCKET -1
#define SOCKET_ERROR -1

#define ADDRESS "127.0.0.1" /* localhost address */
#define PORT 12345
#define BUFFER_SIZE 1024

static void initializeSocket(SOCKET* sock);
static void sendMessageToServer(const SOCKET sock, const char* buffer);
static void waitForAnswerFromServer(const SOCKET sock, char* outputBuffer);
static void closeSocket(SOCKET sock);

#endif