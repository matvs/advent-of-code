#include <iostream>
#include <string>
#include <algorithm>

#include <sstream>
#include <vector>
#include <iterator>

#include <fstream>

using namespace std;

template <typename Out>
void split(const std::string& s, char delim, Out result) {
    std::istringstream iss(s);
    std::string item;
    while (std::getline(iss, item, delim)) {
        *result++ = item;
    }
}

std::vector<std::string> split(const std::string& s, char delim) {
    std::vector<std::string> elems;
    split(s, delim, std::back_inserter(elems));
    return elems;
}

struct PasswordPolicy {
    char requiredCharacter;
    int min;
    int max;

    PasswordPolicy(char requiredCharacter, int min, int max) {
        this->requiredCharacter = requiredCharacter;
        this->min = min;
        this->max = max;
    }

    bool isValid(string password) {
        // TODO: maybe would be better to use regex.
        int count = 0;
        for (string::iterator c = password.begin(); c != password.end(); ++c) {
            if ((*c) == this->requiredCharacter) {
                count++;
            }
        }

        return count >= this->min && count <= this->max;
    }

     bool isValidForTobogganCorporate(string password) {
        // without validation if indexes are out of bound.
        // maybe one could use XOR
        return password[this->min - 1] != password[this->max - 1] && (password[this->min - 1] == this->requiredCharacter || password[this->max - 1] == this->requiredCharacter);
    }
};

int main(int argc, char* argv[]) {
    std::ifstream infile("task2Input.txt");
    cout << "Password Philosophy\n";
    std::string line;
    int count = 0;
    int countPart2 = 0;
    while (std::getline(infile, line)) {
        vector<string> tokens = split(line, ' ');

        vector<string> minMax = split(tokens[0], '-');
        int min = stoi(minMax[0].c_str());
        int max = stoi(minMax[1].c_str());


        char requiredCharacter = tokens[1][0];

        string password = tokens[2];

        PasswordPolicy* policy = new PasswordPolicy(requiredCharacter, min, max);
        if (policy->isValid(password)) {
            count++;
        }

        // part2 
        if (policy->isValidForTobogganCorporate(password)) {
            countPart2++;
        }
    }
    cout << count << endl;
    cout << countPart2 << endl;
    return 0;
}