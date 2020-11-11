#include <iostream>
#include <string>
#include <algorithm>

#include <sstream>
#include <vector>
#include <iterator>

#include <fstream>

using namespace std;


template <typename Out>
void split(const std::string &s, char delim, Out result) {
    std::istringstream iss(s);
    std::string item;
    while (std::getline(iss, item, delim)) {
        *result++ = item;
    }
}

std::vector<std::string> split(const std::string &s, char delim) {
    std::vector<std::string> elems;
    split(s, delim, std::back_inserter(elems));
    return elems;
}


int main(int argc, char* argv[]) {
  std::ifstream infile("task2Input.txt");
  cout << "Hello Santa!\n";
    std::string line;
    int total = 0;
    while (std::getline(infile, line))
    {
//        vector<string> dimensions;
        vector<string> dimensions = split(line, 'x');
//        transform(dimensions.begin(), dimensions.end(), null, [](string num){return atoi(num..c_str());});
        int l = atoi(dimensions[0].c_str());
        int w = atoi(dimensions[1].c_str());
        int h = atoi(dimensions[2].c_str());
        
        vector<int> dimensionsInt;
        for(vector<string>::iterator it = dimensions.begin(); it != dimensions.end(); ++it) {
            dimensionsInt.push_back(atoi((*it).c_str()));
        }
        
        
        sort(dimensionsInt.begin(), dimensionsInt.end());
//        cout << dimensionsInt[0] << " " << dimensionsInt[1] << endl;;
//        total += 2 * ( l*w + l*h + w*h) + dimensionsInt[0]*dimensionsInt[1];

//        part 2
          total += l*w*h + 2*(dimensionsInt[0]+dimensionsInt[1]);
//        cout << l << 'x' << w << 'x' << h << endl;

        // process pair (a,b)
    }
    cout << "Answer: " << total <<endl;

}
