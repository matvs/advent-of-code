#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <fstream>

using namespace std;

class Stream {
public:
    int currentIndex;

    Stream(int size) : preambleSize(size), currentIndex(0) {}

    vector<int> getNumbers() {
        return numbers;
    }

    void add(int x) {
        numbers.push_back(x);
    }

    int nextValue() {
        return numbers[currentIndex++];
    }

    void next() {
        currentIndex++;
    }

    int current() {
        return numbers[currentIndex];
    }

    bool hasNext() {
        return currentIndex < numbers.size() - 1;
    }

    bool isFinished() {
        return currentIndex >= numbers.size();
    }

    // TODO: it could accept a function as param
    bool isValid() {
        if (currentIndex < preambleSize)
        {
            return true;
        }
        // could use map (dict) for O(n) complexity (lke in day one)

        // Jesus Christ, this is a mess.
        // auto begin = numbers.begin();
        // advance(begin, currentIndex - preambleSize);

        // auto end = numbers.begin();
        // advance(end, currentIndex);

        // for (auto i = begin; i != end; ++i) {
        //     for ( auto j = ; j != end; ++j) {

        //         if ((*i) + (*j) == current()) {
        //             return true;
        //         }
        //     }
        // }

        for (int i = currentIndex - preambleSize; i < currentIndex; ++i) {
            for (auto j = i + 1; j < currentIndex; ++j) {
                if ((numbers[i]) + (numbers[j]) == current()) {
                    return true;
                }
            }
        }
        return false;
    }

private:
    vector<int> numbers;
    int preambleSize;
};

int breakCipher(int target, Stream* input) {
    auto data = input->getNumbers();
    for (int i = 0; i < data.size(); ++i) {
        int currentSum = 0;
        vector<int> continousSet;
        for (auto j = i; j < data.size(); ++j) {
            currentSum += data[j];
            continousSet.push_back(data[j]);
            if (currentSum == target) {
                return *(max_element(continousSet.begin(), continousSet.end())) + *(min_element(continousSet.begin(), continousSet.end()));
            }
        }
        }
}

int main(int argc, char *argv[]) {
    ifstream infile("task9Input.txt");
    cout << "Encoding Error\n";
    string line;
    Stream *stream = new Stream(25);
    int firstInvalidNumber;

    while (std::getline(infile, line)) {
        stream->add(atoi(line.c_str()));
    }

    while (!stream->isFinished()) {
        // cout << stream->current() << endl;
        if (!stream->isValid()) {
            cout << stream->current() << endl;
            firstInvalidNumber = stream->current();
            break;
        }
        stream->next();
    }

    cout << breakCipher(firstInvalidNumber, stream);
    return 0;
}
