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
  string registerName;
  string value;
  static Instruction* parse(string instruction) {
    Instruction* instructionObj = new Instruction();
    vector<string> tokens = split(instruction, ' ');
    instructionObj->opcode = tokens[0];
      if(instructionObj->opcode != "jmp") {
        if (instructionObj->opcode == "jie" || instructionObj->opcode == "jio") {
          instructionObj->registerName = tokens[1].substr(0, tokens[1].length() - 1);
          instructionObj->value = tokens[2];
        } else {
          instructionObj->registerName = tokens[1];
        }
  
      } else {
        instructionObj->value = tokens[1];
      }
    return instructionObj;
  }

  void print() {
      cout<< this->opcode << " " << this->registerName << " " << this->value << endl;
  }
};


class Program {
  public:
  map<string, Register*> registers = {
    {"a", new Register("a")},
    {"b", new Register("b")},
  };
  vector<Instruction*> program;
  int counter = 0;

  Program( vector<Instruction*> program) {
    this->program = program;
  }

  void run() {
    this->counter = 0;
    while(this->counter < program.size()) {
      Instruction* instruction = this->program[this->counter];
      // instruction->print();
      this->run(instruction->opcode, instruction->registerName, instruction->value);
    }
  }

  private:
  //   hlf r sets register r to half its current value, then continues with the next instruction.
//   tpl r sets register r to triple its current value, then continues with the next instruction.
//   inc r increments register r, adding 1 to it, then continues with the next instruction.
//   jmp offset is a jump; it continues with the instruction offset away relative to itself.
//   jie r, offset is like jmp, but only jumps if register r is even ("jump if even").
//   jio r, offset is like jmp, but only jumps if register r is 1 ("jump if one", not odd).
  void run(string opcode, string registerName, string value) {
      if(opcode == "hlf") {
        // registers[registerName] /= 2;
        registers[registerName] = *registers[registerName] / 2;
        this->counter++;
      } else if(opcode == "tpl") {
        // registers[registerName] *= 3;
        registers[registerName] =  *registers[registerName] * 3;
        this->counter++;
      } else if(opcode == "inc") {
        registers[registerName] =  *registers[registerName] + 1;
        this->counter++;
      } else if(opcode == "jmp") {
        this->counter += stoi(value);
      } else if(opcode == "jie") {
        if (registers[registerName]->read() % 2 == 0) {
           this->counter += stoi(value);
        } else {
            this->counter++;
        }
      } else if(opcode == "jio") {
         if (registers[registerName]->read() == 1) {
           this->counter += stoi(value);
        } else {
            this->counter++;
        }
      } else {
        throw 404;
      }

      // cout<<this->counter << endl;
  }
};


int main(int argc, char* argv[]) {
  std::ifstream infile("task23Input.txt");
  cout << "Opening the Turing Lock !\n";
  std::string line;
   vector<Instruction*> instructions;
  while (std::getline(infile, line)) {
      instructions.push_back(Instruction::parse(line));
    }

  // for(vector<Instruction*>::iterator it = instructions.begin(); it != instructions.end(); ++it) {
  //   (*it)->print();        
  // }

  Program* program = new Program(instructions);
  program->run();
  cout << program->registers["b"]->read() << endl;


  // part2;
   program->registers["b"]->write(0);
   program->registers["a"]->write(1);
  program->run();
  cout << program->registers["b"]->read() << endl;
}



