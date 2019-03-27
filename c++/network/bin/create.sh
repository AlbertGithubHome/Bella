#echo "g++ -std=c++0x -O2 -Wall -pedantic -pthread "$1
#g++ -std=c++0x -O2 -Wall -pedantic -pthread $1
echo "g++ -std=c++0x -O2 -Wall -pedantic -m32 -pthread "$1 "-o "$2
g++ -std=c++0x -O2 -Wall -pedantic -pthread -m32 $1 -o $2
