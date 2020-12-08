#include <iostream>
#include <string>
#include <fstream>
#include <iterator>
#include <map>
#include <vector>
#include <regex>
#include <sstream>
#include <algorithm> 
#include <functional> 
#include <cctype>
#include <locale>
#include <queue>
#include <stack>

using namespace std;


// trim from start
static inline std::string& ltrim(std::string& s) {
    s.erase(s.begin(), std::find_if(s.begin(), s.end(),
        std::not1(std::ptr_fun<int, int>(std::isspace))));
    return s;
}

// trim from end
static inline std::string& rtrim(std::string& s) {
    s.erase(std::find_if(s.rbegin(), s.rend(),
        std::not1(std::ptr_fun<int, int>(std::isspace))).base(), s.end());
    return s;
}

// trim from both ends
static inline std::string& trim(std::string& s) {
    return ltrim(rtrim(s));
}
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

class Node {
public:
    bool visited = false;
    bool processed = false;
    int multiplier = 1;
    Node* parent;
    string label;
    // TODO refactor it later https://soundcloud.com/espen-sande-larsen-365984601/refactor
    map<string, int> neighboursMetaData;

    void connectWith(Node* node) {
        adjacentList.push_back(node);
    }

    vector<Node*> getNeighbours() {
        return adjacentList;
    };

private:
    vector<Node*> adjacentList;
};


class Graph {
public:

    void addDirectedEdge(string fromLabel, string toLabel) {
        Node* fromNode = getByLabel(fromLabel);
        Node* toNode = getByLabel(toLabel);
        fromNode->connectWith(toNode);
    }

    void addDirectedEdge(string fromLabel, string toLabel, int metadata) {
        Node* fromNode = getByLabel(fromLabel);
        fromNode->neighboursMetaData[toLabel] = metadata;
        addDirectedEdge(fromLabel, toLabel);
    }

    // TODO: write generic traverse method.
    int BFS(string startLabel) {
        Node* startNode = getByLabel(startLabel);
        int counter = 0;

        for (auto it = nodes.begin(); it != nodes.end(); ++it) {
            // cout << it->first << "  " << it->second->getNeighbours().size() << endl;
            it->second->visited = false;
            it->second->processed = false;
        }

        queue<Node*> q;
        q.push(startNode);

        while (q.size() > 0) {
            counter++;
            Node* nextNode = q.front();
            q.pop();
            nextNode->visited = true;
            vector<Node* > neighbours = nextNode->getNeighbours();

            for (auto it = neighbours.begin(); it != neighbours.end(); ++it) {
                if ((*it)->visited == false && (*it)->processed == false) {
                    (*it)->processed = true;
                    q.push(*it);
                }
            }
        }

        return counter;
    }

    //  int DFS(string startLabel) {
    //     Node* startNode = getByLabel(startLabel);
    //     int counter = 0;

    //     for (auto it = nodes.begin(); it != nodes.end(); ++it) {
    //         // cout << it->first << "  " << it->second->getNeighbours().size() << endl;
    //         it->second->visited = false;
    //         it->second->processed = false;
    //         it->second->multiplier = 1;
    //         it->second->parent = NULL;
    //     }

    //     stack<Node*> s;
    //     s.push(startNode);

    //     while (s.size() > 0) {
    //         Node* nextNode = s.top();
    //         s.pop();
    //         nextNode->visited = true;
    //         vector<Node* > neighbours = nextNode->getNeighbours();

    //         for (auto it = neighbours.begin(); it != neighbours.end(); ++it) {
    //             if ((*it)->visited == false && (*it)->processed == false) {
    //                 (*it)->processed = true;
    //                 (*it)->parent = nextNode;
    //                 // counter += nextNode->neighboursMetaData[(*it)->label] * nextNode->multiplier;
    //                 //cout << nextNode->label << "->" << (*it)->label << " " << nextNode->neighboursMetaData[(*it)->label] << " " << endl;
    //                 // (*it)->multiplier =  nextNode->neighboursMetaData[(*it)->label] * nextNode->multiplier;
    //                 s.push(*it);
    //             }
    //         }
    //     }


    //     for (auto it = nodes.begin(); it != nodes.end(); ++it) {
    //         Node* currentNode = it->second;

    //     }

    //     return counter;
    // }

    int DFSEachSeperately(string startLabel, int multiplier) {
        Node* startNode = getByLabel(startLabel);
        int counter = 0;

        vector<Node* > neighbours = startNode->getNeighbours();

        for (auto it = neighbours.begin(); it != neighbours.end(); ++it) {
            // cout << startNode->label << "->" << (*it)->label << " " << startNode->neighboursMetaData[(*it)->label] << " mul by " << multiplier << endl;
            counter += startNode->neighboursMetaData[(*it)->label] * multiplier + DFSEachSeperately((*it)->label,  multiplier * startNode->neighboursMetaData[(*it)->label]);
        }

        return counter;
    }
private:
    map<string, Node*> nodes;

    Node* getByLabel(string label) {
        Node* node;
        map<string, Node*>::iterator it = nodes.find(label);
        if (it == nodes.end()) {
            node = nodes[label] = new Node();
            node->label = label;
        }
        else {
            node = it->second;
        }

        return node;
    }
};




int main(int argc, char* argv[]) {
    ifstream infile("task7Input.txt");
    cout << "Handy Haversacks\n";
    string line;

    string patternMainBag = "([\\w ]+) bags contain (.+)";
    regex mainBagRegex(patternMainBag);

    // string patternContainedBags = "(\\d+([\\w ]+))";
    // regex containedBagsRegex(patternContainedBags);

    smatch sm;

    Graph* graph = new Graph();
    Graph* graphPart2 = new Graph();
    while (std::getline(infile, line)) {
        regex_match(line, sm, mainBagRegex);
        string s = sm[1].str();
        string mainBagLabel = trim(s);
        // cout << mainBagLabel << endl;
        string listOfBagsInside = sm[2].str();
        if (listOfBagsInside == "no other bags.") {
            //  cout << listOfBagsInside << endl;
            continue;
        }
        vector<string> bagsInside = split(listOfBagsInside, ',');
        for (auto it = bagsInside.begin(); it != bagsInside.end(); ++it) {
            //TODO: use regex to support any number of bags, not only single digit ones.
            string label = trim(*it).substr(2);
            if (label.at(label.size() - 1) == '.') {
                label = label.substr(0, label.size() - 1);
            }
            // suffixSize (bag or bags)
            int suffixSize = label.at(label.size() - 1) == 's' ? 5 : 4;
            label = label.substr(0, label.size() - suffixSize);
            // cout << label << endl;

            graph->addDirectedEdge(label, mainBagLabel);

            //part2
            int numberOfBags = atoi(trim(*it).substr(0, 1).c_str());
            // cout << label << " : " << numberOfBags << endl;;
            graphPart2->addDirectedEdge(mainBagLabel, label, numberOfBags);
        }
    }

    string myBagLabel = "shiny gold";
    int howManyBagsMayContainMine = graph->BFS(myBagLabel);
    cout << howManyBagsMayContainMine - 1 << endl;

    int howManyBagsNeedsTobeCarried = graphPart2->DFSEachSeperately(myBagLabel, 1);
    cout << howManyBagsNeedsTobeCarried << endl;

    return 0;
}