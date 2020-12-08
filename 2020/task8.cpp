#include <iostream>
#include <string>
#include <algorithm>

#include <sstream>
#include <vector>
#include <map>
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

class Register {
public:
    Register(string name) {
        this->name = name;
    }

    void write(int v) {
        this->value = v;
    }

    int read() {
        return this->value;
    }

    string getName() {
        return this->name;
    }

    Register* operator *= (int x) {
        this->value *= x;
        return this;
    }

    Register* operator /= (int x) {
        this->value /= x;
        return this;
    }

    Register* operator * (int x) {
        this->value *= x;
        return this;
    }

    Register* operator / (int x) {
        this->value /= x;
        return this;
    }

    Register* operator += (int x) {
        this->value += x;
        return this;
    }

    Register* operator + (int x) {
        this->value += x;
        return this;
    }



private:
    string name;
    int value = 0;

};


class Instruction {
public:
    string opcode;
    string registerName = "accumulator";
    string value;
    bool wasExecuted = false;
    static Instruction* parse(string instruction) {
        Instruction* instructionObj = new Instruction();
        vector<string> tokens = split(instruction, ' ');
        instructionObj->opcode = tokens[0];
        instructionObj->value = tokens[1];
        return instructionObj;
    }

    void print() {
        cout << this->opcode << " " << this->registerName << " " << this->value << endl;
    }
};


class Program {
public:
    map<string, Register*> registers = {
      {"accumulator", new Register("accumulator")},
    };
    vector<Instruction*> program;
    int counter = 0;

    Program(vector<Instruction*> program) {
        this->program = program;
    }

    bool run() {
        this->counter = 0;
        for (auto it = program.begin(); it != program.end(); ++it) {
            (*it)->wasExecuted = false;
        }
        while (this->counter < program.size()) {
            Instruction* instruction = this->program[this->counter];
            // instruction->print();
            if (instruction->wasExecuted) {
                // cout << registers["accumulator"]->read() << endl;
                return false;
            }
            this->run(instruction->opcode, instruction->registerName, instruction->value);
            instruction->wasExecuted = true;
        }
        return true;
    }

private:
    // acc increases or decreases a single global value called the accumulator by the value given in the argument. 
    // jmp jumps to a new instruction relative to itself.
    // nop stands for No OPeration - it does nothing. The instruction immediately below it is executed next.
    void run(string opcode, string registerName, string value) {
        if (opcode == "acc") {
            registers[registerName]->write(registers[registerName]->read() + stoi(value));
            this->counter++;
        } else if (opcode == "jmp") {
            this->counter += stoi(value);
        } else if (opcode == "nop") {
            this->counter++;
        } else {
            throw 404;
        }

        // cout<<this->counter << endl;
    }
};


int main(int argc, char* argv[]) {
    ifstream infile("task8Input.txt");
    cout << "Handheld Halting\n";
    string line;

    vector<Instruction*> instructions;
    while (std::getline(infile, line)) {
        instructions.push_back(Instruction::parse(line));
    }

    Program* program = new Program(instructions);
    program->run();
    cout << program->registers["accumulator"]->read() << endl;

    // part2
    Instruction* prevChanged = NULL;

    for (auto it = program->program.begin(); it != program->program.end(); ++it) {
        if ((*it)->opcode == "jmp" || (*it)->opcode == "nop") {
            if (prevChanged != NULL) {
                prevChanged->opcode = prevChanged->opcode == "jmp" ? "nop" : "jmp";
            }
            (*it)->opcode = (*it)->opcode == "jmp" ? "nop" : "jmp";
            prevChanged = *it;
            program->registers["accumulator"]->write(0);
            if (program->run()) {
                cout << program->registers["accumulator"]->read() << endl;
                break;
            }
        }
    }

    return 0;
}
