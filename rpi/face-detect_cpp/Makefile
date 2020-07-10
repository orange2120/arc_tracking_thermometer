CC = g++
CFLAGS = -std=c++11 -fexceptions -Wall

OPENCV = `pkg-config --libs --cflags opencv4`
LIBS = $(OPENCV) -I/usr/local/lib/ /usr/local/lib/libMNN.so
INCS = -I/usr/local/include/MNN 

LDFLAGS += -lpthread
OPTFLAGS = -O3
# OPTFLAGS = -g
# DBGFLAGS = -g

TARGET = MNN_UltraFace.o main
.PHONY: all clean

all: $(TARGET)

main: main.cpp MNN_UltraFace.o 
	$(CC) $(CFLAGS) $^ $(LIBS) $(INCS) $(OPTFLAGS) $(LDFLAGS) -o $@

main_ser: main_ser.cpp MNN_UltraFace.o 
	$(CC) $(CFLAGS) $^ $(LIBS) $(INCS) $(OPTFLAGS) $(LDFLAGS) -o $@

MNN_UltraFace.o: MNN_UltraFace.cpp MNN_UltraFace.hpp
	$(CC) $(CFLAGS) $(OPTFLAGS) $(LIBS) $(INCS) -c $< -o $@

clean:
	rm -f $(TARGET) *.o

