#include <iostream>
#include <string>
#include <vector>
#include <fstream>

using namespace std;

struct Step {
    int x;
    int y;
    Step(int x, int y) : x(x), y(y) {}
};

struct Row {
    Row(string data) {
        this->data = data;
    }

    int getSize() {
        return this->data.length();
    }

    char getObjectAt(int i) {
        return this->data.at(i % this->getSize());
    }

private:
    string data;
};

struct Grid {
    vector<Row*> rows;
    int x;
    int y;

    void addRow(Row* row) {
        this->rows.push_back(row);
        this->x = 0;
        this->y = 0;
    }

    void move(int stepX, int stepY) {
        this->x += stepX;
        this->y += stepY;
    }
    char getObject() {
        return this->getObject(this->x, this->y);
    }

    char getObject(int x, int y) {
        return this->rows[y]->getObjectAt(x);
    }

    bool reachedTheBottom() {
        return this->y >= rows.size();
    }

    int traverseAndCountObjects(int stepX, int stepY, char object) {
        int objectCount = 0;
        while (!this->reachedTheBottom()) {
            if (this->getObject() == object) {
                objectCount++;
            }
            this->move(stepX, stepY);
        }
        return objectCount;
    }

    int traverseAndCountTrees(int stepX, int stepY) {
        return this->traverseAndCountObjects(stepX, stepY, Grid::TREE);
    }

    void reset() {
        this->x = 0;
        this->y = 0;
    }


    static const char TREE = '#';
    static const char EMPTY = '.';
};

int main(int argc, char* argv[]) {
    std::ifstream infile("task3Input.txt");
    cout << "Toboggan Trajectory\n";
    Grid* grid = new Grid();
    std::string line;
    int treeCount = 0;
    while (std::getline(infile, line)) {
        grid->addRow(new Row(line));
    }

    const int stepX = 3;
    const int stepY = 1;
    treeCount = grid->traverseAndCountTrees(stepX, stepY);

    cout << treeCount << endl;

    //part 2
    Step steps[4] = { Step(1,1), Step(5,1), Step(7,1), Step(1,2) };
    for (const Step step : steps) {
        grid->reset();
        treeCount *= grid->traverseAndCountTrees(step.x, step.y);
    }
    cout << treeCount << endl;

    return 0;
}