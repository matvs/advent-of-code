#include <iostream>
#include <string>
#include <algorithm>

#include <sstream>
#include <vector>
#include <iterator>
#include <map>

#include <fstream>

using namespace std;

// TODO: generalize to n terms
void findThreeTerms(map<int, bool> numbers, int targetSum) {
    bool finished = false;
    for (map<int, bool>::iterator item = numbers.begin(); item != numbers.end() && !finished; ++item) {
        int a = item->first;
        int secondTarget = targetSum - a;
        for (map<int, bool>::iterator secondItem = next(item, 1); secondItem != numbers.end(); ++secondItem) {
            int b = secondItem->first;
            int c = secondTarget - b;

            map<int, bool>::iterator foundItem = numbers.find(c);
            if (foundItem != numbers.end()) {
                cout << "Answer (three terms): " << a * b * c << endl;
                finished = true;
                break;
            }
        }
    }
}

int main(int argc, char* argv[]) {
    std::ifstream infile("task1Input.txt");
    cout << "Report Repair\n";
    std::string line;
    vector<int> numbers;
    map<int, bool> numbersMap;
    const int targetSum = 2020;
    while (std::getline(infile, line)) {
        numbers.push_back(atoi(line.c_str()));
        numbersMap.insert(pair<int, bool>(atoi(line.c_str()), true));
    }

    // bruteforce solution - O(n*n)
    bool finished = false;
    for (vector<int>::iterator i = numbers.begin(); i != numbers.end() && !finished; ++i) {
        for (vector<int>::iterator j = next(i, 1); j != numbers.end(); ++j) {
            if (((*i)) + (*j) == targetSum) {
                cout << "Answer (bruteforce): " << (*i) * (*j) << endl;
                finished = true;
                break;
            }
        }
    }

    // O(n) solution
    for (map<int, bool>::iterator item = numbersMap.begin(); item != numbersMap.end(); ++item) {
        int a = item->first;
        int b = targetSum - a;
        map<int, bool>::iterator foundItem = numbersMap.find(b);
        if (foundItem != numbersMap.end()) {
            cout << "Answer O(n): " << a * b << endl;
            break;
        }
    }

    // Part two
    findThreeTerms(numbersMap, targetSum);
}
