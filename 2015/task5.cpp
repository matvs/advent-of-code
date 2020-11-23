#include <iostream>
#include <string>
#include <algorithm>

#include <sstream>
#include <iterator>
#include <regex>

#include <fstream>

using namespace std;


bool isStringNice(string input) {
    const int minNumberOfVowels = 3;
    smatch sm;
   //required
    int numberOfFoundVowels = 0;

    regex vowels("[aeiou]");
    sregex_iterator iter(input.begin(), input.end(), vowels);
    sregex_iterator end;

    while(iter != end)
    {
       ++numberOfFoundVowels;
       iter++;
    }

    regex doubled("([a-zA-Z])\\1");
    regex_search(input,sm,doubled);
    int numberOfDoubled = sm.size();

    //forbidden
    regex forbidden("ab|cd|pq|xy");
    regex_search(input,sm,forbidden);
    if (sm.size() > 0) {
        return false;
    } else if(numberOfFoundVowels >= minNumberOfVowels && numberOfDoubled > 0) {
        return true;
    }

    return false;

}

bool isStringNice2(string input) {
    smatch sm;
    regex overlapped("([a-zA-Z])([a-zA-Z]).*\\1\\2");
    regex_search(input,sm,overlapped);
    int numberOfOverlapped = sm.size();

    regex repeatedAndBetween("([a-zA-Z])[a-zA-Z]\\1");
    regex_search(input,sm,repeatedAndBetween);
    int numberOfRepeatedAndBetween = sm.size();

    if (numberOfOverlapped && numberOfRepeatedAndBetween) {
        return true;
    }

    return false;

}


int main(int argc, char* argv[]) {
  std::ifstream infile("task5Input.txt");
  cout << "Doesn't He Have Intern-Elves For This?\n";
    std::string line;
    int numberOfNice = 0;
    int numberOfNice2 = 0;
      while (std::getline(infile, line)) {
          if (isStringNice(line)) {
              numberOfNice++;
          }
        if (isStringNice2(line)) {
              numberOfNice2++;
          }
    }
    cout <<numberOfNice << endl;
    cout <<numberOfNice2 << endl;
   
    return 0;
}



