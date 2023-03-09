#include "../Domain/Util.h"
#include<iostream>
#include <utility>
using namespace std;
Util::Util() = default;
Util::Util(int id, string nume,int varsta) {
    this->id=id;
    this->vasrta=varsta;
    this->nume = std::move(nume);
}
Util::Util(const Util &util) {
    this->id=util.id;
    this->vasrta=util.vasrta;
    this->nume = util.nume;
}

int Util::getid() const {
    return this->id;
}
string Util::getnume() {
    return this->nume;
}
int Util::getvarsta() const {
    return this->vasrta;
}

void Util::setid(int Id) {
    this->id=Id;
}
void Util::setnume(string num) {
    this->nume=std::move(num);

}
void Util::setvarsta(int vars) {
    this->vasrta=vars;
}


Util &Util::operator=(const Util& util) {
    if (this != &util){
        this->nume=util.nume;
        this->id = util.id;
        this->vasrta=util.vasrta;}
    return *this;
}

bool Util::operator==(const Util& util) {
    return (nume==util.nume) && (this->id == util.id) && (this->vasrta == util.vasrta);
}

ostream& operator<<(ostream &os, Util &util){
    os << util.id << ' ' << util.nume<<' '<<util.vasrta;
    return os;
}

bool Util::operator>(const Util &u) const {
    return this->id>u.id;
}

bool Util::operator<(const Util &u) const {
    return this->id>u.id;
}
