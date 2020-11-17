#include <iostream>
#include <string>
#include <algorithm>

#include <sstream>
#include <vector>
#include <map>
#include <iterator>

#include <fstream>

using namespace std;

class DeliverGuy {
  public: 
  DeliverGuy() {
    this->numberOfVisits = {
      {"0:0", 1}
    };
    this->x = 0;
    this->y = 0;
  }

  move(char direction) {
       map<string, int>::iterator it;
       switch (direction) {
        case '<': {
          this->x -= 1; 
          // cout << "left ";   
          break;
      }
        case '>': {
          this->x += 1;
          // cout << "right "; 
          break;
        }
        case '^': {
          this->y += 1; 
          // cout << "up ";
          break;
        }
        case 'v': {
          this->y -= 1; 
          // cout << "down ";
          break;
        }
    }

    string coords = to_string(this->x) + ':' + to_string(this->y);
    it = this->numberOfVisits.find(coords);
    if (it != this->numberOfVisits.end()) {
      this->numberOfVisits[coords] += 1;
    } else {
       this->numberOfVisits[coords] = 1;
  }
  }

  map<string, int> getNumberOfVisits() {
    return this->numberOfVisits;
  }

  private:
    map<string, int> numberOfVisits; 
    int x;
    int y;

};

 map<string, int> merge(map<string, int> a,  map<string, int> b) {
    map<string, int> merged = {};
     
    for(map<string, int>::iterator it = a.begin(); it != a.end(); ++it) {
       merged[it->first] = it->second; 
    }

    for(map<string, int>::iterator it = b.begin(); it != b.end(); ++it) {
       merged[it->first] = it->second; 
    }

    return merged;
}


int main(int argc, char* argv[]) {
  std::ifstream infile("task3Input.txt");
  cout << "Perfectly Spherical Houses in a Vacuum !\n";
    std::string line;
    std::getline(infile, line);

    int x = 0;
    int y = 0;

    // map<char, int> horizontalSteps = {
    //   {'<', -1},
    //   {'>', 1},
    // };
    
    // map<char, int> verticalSteps = {
    //   {'^', 1},
    //   {'v', -1},
    // };

    map<string, int> numberOfVisits = {
      {"0:0", 1}
    };

    map<string, int>::iterator it;

    for(string::iterator direction = line.begin(); direction != line.end(); ++direction) {
      switch (*direction) {
        case '<': {
          x -= 1; 
          // cout << "left ";   
          break;
      }
        case '>': {
          x += 1;
          // cout << "right "; 
          break;
        }
        case '^': {
          y += 1; 
          // cout << "up ";
          break;
        }
        case 'v': {
          y -= 1; 
          // cout << "down ";
          break;
        }
    }

    string coords = to_string(x) + ':' + to_string(y);
    it = numberOfVisits.find(coords);
    if (it != numberOfVisits.end()) {
      numberOfVisits[coords] += 1;
    } else {
      numberOfVisits[coords] = 1;
    }
    // cout << x << ' ' << y;  
  }

  cout << numberOfVisits.size() << endl;


  // part2 

DeliverGuy* santa = new DeliverGuy();
DeliverGuy* roboSanta = new DeliverGuy();
bool santasTurn = true;

for(string::iterator direction = line.begin(); direction != line.end(); ++direction) {
      if (santasTurn) {
        santa->move(*direction);
      } else {
        roboSanta->move(*direction);
      }

      santasTurn = !santasTurn;
  }

  
  cout << merge(santa->getNumberOfVisits(), roboSanta->getNumberOfVisits()).size();
}



