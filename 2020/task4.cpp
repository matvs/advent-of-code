#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <fstream>
#include <sstream>
#include <regex>
#include <iterator>

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

struct Validator {
    int min;
    int max;
    string pattern;
    vector<string> allowedValues;

    Validator(int min, int max, string pattern, vector<string> allowedValues) : min(min), max(max), pattern(pattern), allowedValues(allowedValues) {}
    Validator(int min, int max) : min(min), max(max), pattern("") {}
    Validator(vector<string> allowedValues) : allowedValues(allowedValues) {}
    Validator(string pattern) : pattern(pattern) {}

    bool validate(string value) {
        if (allowedValues.size() > 0) {
            return find(allowedValues.begin(), allowedValues.end(), value) != allowedValues.end();
        }
        if (pattern != "") {
            regex patternRegex(pattern);
            return regex_match(value, patternRegex);
        }

        int valueInt = atoi(value.c_str());
        return valueInt >= min && valueInt <= max;

    }
};

class Passport {
public:
    static map<string, string> FEATURES;
    // Wow, this sucks, that there is no easy way to get an vector of map keys in C++. 
    static vector<string> FEATURES_KEYS;
    static vector<string> OPTIONAL;

    void addFeature(string key, string value) {
        if (Passport::FEATURES.find(key) != Passport::FEATURES.end()) {
            features.insert(pair<string, string>(key, value));
            featuresKeys.push_back(key);
        }
        else {
            // TODO: maybe throw exception or addFeature could return bool value.
        }

    }

    bool isValid() {
        //For part one only hasAllRequiredFields condition needs to be checked.
        return hasAllRequiredFields() && validateFields();
    }

private:
    map<string, string> features;
    // Wow, this sucks, that there is no easy way to get an vector of map keys in C++. 
    vector<string> featuresKeys;
    static map<string, Validator*> VALIDATORS;

    bool validateFields() {
        for (vector<string>::iterator key = featuresKeys.begin(); key != featuresKeys.end(); ++key) {
            map<string, Validator*>::iterator validator = Passport::VALIDATORS.find(*key);
            if (validator != Passport::VALIDATORS.end()) {
                // cout << *key << " " << features[*key] << " " << validator->second->validate(features[*key]) << endl;
                if (!(validator->second->validate(features[*key]))) {
                    return false;
                }

                //special case
                if (*key == "hgt") {
                    std::smatch sm;    // same as std::match_results<const char*> cm;
                    regex e("(\\d+)(cm|in)");
                    string value = features[*key];
                    regex_match(value, sm, e);
                    if (sm[2] == "cm") {
                        if (!((new Validator(150, 193))->validate(sm[1]))) {
                            return false;
                        }
                    } else {
                        // previous validation guarantees that it is "in" (inches)
                        if (!((new Validator(59, 76))->validate(sm[1]))) {
                            return false;
                        }
                    }

                }
            }
        }
        return true;
    }

    bool hasAllRequiredFields() {
        // Due to constraint in addFeature method it can only contains valid key-value pairs.
        int numberOfOptional = 0;
        for (vector<string>::iterator key = Passport::OPTIONAL.begin(); key != Passport::OPTIONAL.end(); ++key) {
            if (find(featuresKeys.begin(), featuresKeys.end(), *key) != featuresKeys.end()) {
                numberOfOptional++;
            }
        }

        int minNumberOfRequired = Passport::FEATURES_KEYS.size() - Passport::OPTIONAL.size();
        return featuresKeys.size() - numberOfOptional == minNumberOfRequired;
    }


};

// byr (Birth Year) - four digits; at least 1920 and at most 2002.
// iyr (Issue Year) - four digits; at least 2010 and at most 2020.
// eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
// hgt (Height) - a number followed by either cm or in:
// If cm, the number must be at least 150 and at most 193.
// If in, the number must be at least 59 and at most 76.
// hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
// ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
// pid (Passport ID) - a nine-digit number, including leading zeroes.
// cid (Country ID) - ignored, missing or not.
map<string, Validator*> Passport::VALIDATORS = {
        {"byr", new Validator(1920, 2002)},
        {"iyr", new Validator(2010, 2020)},
        {"eyr", new Validator(2020, 2030)},
        //  {"hgt", "Height"}, special case
        { "hgt", new Validator("\\d+(cm|in)")},
        {"hcl", new Validator("#([\\dabcdef]{6,6})")},
        {"ecl", new Validator(vector<string> {"amb", "blu", "brn", "gry", "grn",  "hzl", "oth"})},
        {"pid",  new Validator("\\d{9,9}")},
        // {"cid", "Country ID"}
};

map<string, string> Passport::FEATURES = {
        {"byr", "Birth Year"},
        {"iyr", "Issue Year"},
        {"eyr", "Expiration Year"},
        {"hgt", "Height"},
        {"hcl", "Hair Color"},
        {"ecl", "Eye Color"},
        {"pid", "Passport ID"},
        {"cid", "Country ID"}
};

vector<string> Passport::OPTIONAL = { "cid" };
vector<string> Passport::FEATURES_KEYS = { "byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid" };

int main(int argc, char* argv[]) {
    std::ifstream infile("task4Input.txt");
    cout << "Passport Processing\n";
    std::string line;
    int numberOfValidPassports = 0;
    Passport* passport = new Passport();
    int i = 0;
    while (std::getline(infile, line)) {
        if (line == "") {
            if (passport->isValid()) {
                numberOfValidPassports++;
            }
            passport = new Passport();
        } else {
            vector<string> tokens = split(line, ' ');
            for (vector<string>::iterator it = tokens.begin(); it != tokens.end(); ++it) {
                vector<string> keyValuePair = split(*it, ':');
                passport->addFeature(keyValuePair[0], keyValuePair[1]);
            }
        }
    }

    if (passport->isValid()) {
        numberOfValidPassports++;
    }
    cout << numberOfValidPassports << endl;

    return 0;
}