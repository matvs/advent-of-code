#include <iostream>
#include <string>
#include <algorithm>

#include <sstream>
#include <vector>
#include <map>
#include <iterator>

#include <fstream>

using namespace std;


bool isStringNice(string input) {
    vector<string> required = {
        "a",
        "e",
        "i",
        "o",
        "u",
        };
    int minOccuranceOfRequired = 3;
    int requiredOcuurances = 0;

    for (vector<string>::iterator it = required.begin(); it != required.end(); ++it) {
        size_t found = -1;
        // cout << *it << endl;
        do {
           found = input.find(*it, found == -1 ? 0 : found + 1);
            //    cout << found << endl << input << endl;
            if (found != std::string::npos) {
                requiredOcuurances++;
            }
               if (requiredOcuurances >= minOccuranceOfRequired) {
           break;
       }
        } while (found!=std::string::npos);
       if (requiredOcuurances >= minOccuranceOfRequired) {
           break;
       }
        
    }

    string twoChars = "";
    int twoInRow = 0;
        for (string::iterator it = input.begin(); it != input.end(); ++it) {
            if (twoChars.length() == 2) {
                // cout << twoChars <<  " ";
                if (twoChars[0] == twoChars[1]) {
                    twoInRow++;
                    break;
                }
                twoChars = "";
                it--;
            }

            twoChars += *it;
        
    }

     if (twoChars.length() == 2) {
                // cout << twoChars <<  " ";
                if (twoChars[0] == twoChars[1]) {
                    twoInRow++;
               
                }
          
            }

        vector<string> forbidden = {
        "ab",
        "cd",
        "pq",
        "xy",
        };

         int maxOccuranceOfForbidden = 1;

             for (vector<string>::iterator it = forbidden.begin(); it != forbidden.end(); ++it) {
        size_t found = -1;
   
           found = input.find(*it, found == -1 ? 0 : found + 1);
            if (found != std::string::npos) {
                return false;
            }
         
        
    }
        //  cout << requiredOcuurances << minOccuranceOfRequired << twoInRow << endl;
       if (requiredOcuurances >= minOccuranceOfRequired && twoInRow >=1) {
           return true;
       }

       return false;
 

}

int main(int argc, char* argv[]) {
  std::ifstream infile("task5Input.txt");
  cout << "Doesn't He Have Intern-Elves For This?\n";
    std::string line;
    int numberOfNice = 0;
      while (std::getline(infile, line)) {
          if (isStringNice(line)) {
              numberOfNice++;
          }
    }
    // cout << isStringNice("arehecc") << endl;;
    cout <<numberOfNice;
}



