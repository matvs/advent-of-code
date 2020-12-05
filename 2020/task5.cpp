#include <iostream>
#include <string>
#include <math.h>   
#include <fstream>
#include <iterator>

using namespace std;

struct Seat {
    string rowPath;
    string colPath;

    Seat(string rowPath, string colPath) : rowPath(rowPath), colPath(colPath) {
        // cout << rowPath << " " << colPath << endl;
    }

    int getRow() {
        return getPos(0, 127, rowPath, Seat::rowLowerHalf, Seat::rowUpperHalf);
    }

    int getCol() {
        return getPos(0, 7, colPath, Seat::colLowerHalf, Seat::colUpperHalf);
    }

    int getId() {
        return getRow() * 8 + getCol();
    }

    // bool isFrontSeat() {
    //     return getId() >= 0 && getId() <= 8;
    // }

    // bool isBackSeat() {
    //     return getId() >= 127 * 8 && getId() <= 127 * 8 + 8;
    // }

    const static char rowLowerHalf = 'F';
    const static char rowUpperHalf = 'B';
    const static char colLowerHalf = 'L';
    const static char colUpperHalf = 'R';

private:
    int getPos(int lowerBound, int upperBound, string path, char lowerHalf, char upperHalf) {
        for (string::iterator move = path.begin(); move != path.end(); ++move) {
            int half = (*move == lowerHalf ? ((upperBound - lowerBound) / 2) : round((upperBound - lowerBound) / 2.0)) + lowerBound;
            if (*move == lowerHalf) {
                upperBound = half;
            } else if (*move == upperHalf) {
                lowerBound = half;
            } else {
                cout << "Input not valid" << endl;
            }
        }
        return path.at(path.size() - 1) == lowerHalf ? lowerBound : upperBound;
    }
};


int main(int argc, char* argv[]) {
    std::ifstream infile("task5Input.txt");
    cout << "Binary Boarding\n";
    std::string line;
    int heighestId = 0;
    const int numberOfSeats = 127 * 8 + 7;
    bool takenSeats[numberOfSeats] = { false };
    while (std::getline(infile, line)) {
        Seat* seat = new Seat(line.substr(0, 7), line.substr(7));
        int seatId = seat->getId();
        heighestId = heighestId < seatId ? seatId : heighestId;

        //part 2
        takenSeats[seat->getId()] = true;
    }

    cout << heighestId << endl;

    // part2
    for (int i = 0; i < numberOfSeats; i++) {
        int prevSeat = i - 1;
        int nextSeat = i + 1;
        if (prevSeat >= 0 && nextSeat < numberOfSeats && !takenSeats[i] && takenSeats[prevSeat] && takenSeats[nextSeat]) {
            cout << i << endl;
        }
    }

    return 0;
}