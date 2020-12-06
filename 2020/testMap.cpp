#include <iostream>
#include <string>
#include <fstream>
#include <iterator>
#include <map>
#include <vector>

using namespace std;

void printMap(map<char, bool> dict) {
    cout << "{ ";
    for (auto keyVal = dict.begin(); keyVal != dict.end(); ++keyVal) {
        cout << keyVal->first << " : " << (keyVal->second ? "true" : "false") << ", ";
    }
    cout << " } " << endl;
}

int main(int argc, char* argv[]) {
    string startInput = "abcdefg";
    string nextInput = "abcf";
    map<char, bool> dict;

    for (auto it = startInput.begin(); it != startInput.end(); it++) {
        dict[*it] = true;
    }
    printMap(dict);

    for (auto keyVal = dict.begin(); keyVal != dict.end(); ++keyVal) {
        cout << keyVal->first;
        cout << endl;
        if (nextInput.find(keyVal->first) == string::npos) {
            // dict.erase(keyVal);
            dict.erase(keyVal->first);
        }
    }
    printMap(dict);
    
    return 0;
}


