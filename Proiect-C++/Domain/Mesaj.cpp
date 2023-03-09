#include "../Domain/Mesaj.h"
#include<iostream>
#include <utility>
using namespace std;
Mesaj::Mesaj() = default;
Mesaj::Mesaj(const Util& util1, const Util& util2, string mesaj) {
    this->mesaj = std::move(mesaj);
    this->util1=util1;
    this->util2=util2;
}
Mesaj::Mesaj(const Mesaj &mes) {
    this->mesaj = mes.mesaj;
    this->util1 = mes.util1;
    this->util2=mes.util2;
}

Util Mesaj::getutil1() {
    return this->util1;
}
string Mesaj::getmesaj() {
    return this->mesaj;
}
Util Mesaj::getutil2() {
    return this->util2;
}

void Mesaj::setutil1(const Util& ut1) {
    this->util1=ut1;
}
void Mesaj::setutil2(const Util& ut2) {
    this->util2=ut2;

}
void Mesaj::setmesaj(string mes) {
    this->mesaj=std::move(mes);
}


Mesaj &Mesaj::operator=(const Mesaj& mes) {
    if (this != &mes){
        this->mesaj=mes.mesaj;
        this->util1=mes.util1;
        this->util2=mes.util2;}
    return *this;
}

bool Mesaj::operator==(const Mesaj& mes) {
    return this->mesaj==mes.mesaj && this->util1 == mes.util1 && this->util2 == mes.util2;
}

ostream& operator<<(ostream &os, Mesaj &mes){
    os << mes.util1 << ' ' << mes.util2<<' '<<mes.mesaj<<'\n';
    return os;
}
