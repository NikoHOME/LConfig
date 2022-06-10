CC=gcc
CFLAGS=-c -O3 -fopenmp -DLODEPNG_NO_COMPILE_DECODER -DLODEPNG_NO_COMPILE_DISK -DLODEPNG_NO_COMPILE_ANCILLARY_CHUNKS -DLODEPNG_NO_COMPILE_ERROR_TEXT -Wall -Wextra
LDFLAGS=-lX11 -fopenmp
DEPS=lodepng/lodepng.h

i3lock-fancier-rapid: i3lock-fancier-rapid.o lodepng.o
	$(CC) $^ $(LDFLAGS) -o $@

i3lock-fancier-rapid.o: i3lock-fancier-rapid.c $(DEPS)
	$(CC) $(CFLAGS) $< -o $@

lodepng.o: lodepng/lodepng.cpp $(DEPS)
	$(CC) $(CFLAGS) -x c $< -o $@

clean:
	rm -f i3lock-fancier-rapid *.o
