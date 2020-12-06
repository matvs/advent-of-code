#include <iostream>
#include <string>
#include <fstream>
#include <iterator>
#include <map>
#include <vector>

using namespace std;

class GroupCustomDeclaration {
public:
    void addYesAnswer(char question) {
        positiveAnswers[question] = true;
    }

    int getNumberOfYesAnswers() {
        return positiveAnswers.size();
    }

    void addYesAnswerInUnison(string questions) {
        if (!isPositiveAnswersInUnisonInitialized) {
            isPositiveAnswersInUnisonInitialized = true;
            for (string::iterator question = questions.begin(); question != questions.end(); ++question) {
                positiveAnswersInUnison[*question] = true;
            }
        } else {
            // WTF in C++ removing elements in map/dictionary/hash table - you name it - works like removing elemnts from dynamic array, vector or list - once again you name it.
            vector<char> toBeRemoved;
            for (auto answer = positiveAnswersInUnison.begin(); answer != positiveAnswersInUnison.end(); ++answer) {
                if (questions.find(answer->first) == string::npos) {
                    // positiveAnswersInUnison.erase(answer);
                    toBeRemoved.push_back(answer->first);
                }
            }
            for (auto it = toBeRemoved.begin(); it != toBeRemoved.end(); ++it) {
                positiveAnswersInUnison.erase(*it);
            }
        }
    }

    int getNumberOfYesAnswersInUnison() {
        return positiveAnswersInUnison.size();
    }

private:
    map<char, bool> positiveAnswers;
    map<char, bool> positiveAnswersInUnison;
    bool isPositiveAnswersInUnisonInitialized = false;
};

int main(int argc, char* argv[]) {
    std::ifstream infile("task6Input.txt");
    cout << "Custom Customs\n";
    std::string line;
    GroupCustomDeclaration* customDeclaration = new GroupCustomDeclaration();
    int totalNumberOfYesAnswers = 0;
    int totalNumberOfYesAnswersPart2 = 0;
    int i = 0;
    while (std::getline(infile, line)) {
        if (line == "") {
            totalNumberOfYesAnswers += customDeclaration->getNumberOfYesAnswers();
            totalNumberOfYesAnswersPart2 += customDeclaration->getNumberOfYesAnswersInUnison();

            customDeclaration = new GroupCustomDeclaration();
        }
        else {
            for (string::iterator question = line.begin(); question != line.end(); ++question) {
                customDeclaration->addYesAnswer(*question);
            }
            customDeclaration->addYesAnswerInUnison(line);
        }
    }
    totalNumberOfYesAnswers += customDeclaration->getNumberOfYesAnswers();
    totalNumberOfYesAnswersPart2 += customDeclaration->getNumberOfYesAnswersInUnison();

    cout << totalNumberOfYesAnswers << endl;
    cout << totalNumberOfYesAnswersPart2 << endl;

    return 0;
}