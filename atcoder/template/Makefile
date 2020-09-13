build: Main.cpp
	g++ -std=gnu++1y -O2 -I/opt/boost/gcc/include -L/opt/boost/gcc/lib -o a.out Main.cpp

run: build
	./a.out

dl:
	rm -rf test
	oj download {DOWNLOAD_URL}

t: build
	oj test
