#include "../Domain/Prietenie.h"
#include<iostream>
using namespace std;
Pri::Pri() {
    this->id=0;
    this->id1=0;
    this->id2=0;
}
Pri::Pri(int id,int id1,int id2) {
    this->id=id;
    this->id1=id1;
    this->id2=id2;
}
Pri::Pri(const Pri &pri) {
    this->id=pri.id;
    this->id1=pri.id1;
    this->id2=pri.id2;
}
int Pri::getid() const {
    return this->id;
}
int Pri::getid1() const {
    return this->id1;
}
int Pri::getid2() const {
    return this->id2;
}
void Pri::setid(int idn) {
    this->id=idn;
}
void Pri::setid1(int idunu) {
    this->id1=idunu;
}
void Pri::setid2(int iddoi) {
    this->id2=iddoi;
}


Pri &Pri::operator=(const Pri& pri) {
    this->id1 = pri.id1;
    this->id2=pri.id2;
    return *this;
}

bool Pri::operator==(const Pri& pri) const {
    return (this->id1 == pri.id1) && (this->id2 == pri.id2);
}

ostream& operator<<(ostream &os, Pri &pri){
    os << pri.id1 << ' ' << pri.id2;
    return os;
}

bool Pri::operator>(const Pri &p) const {
    return this->id>p.id && this->id1<p.id1 && this->id2<p.id2;
}

bool Pri::operator<(const Pri &p) const {
    return this->id<p.id && this->id1<p.id1 && this->id2<p.id2;
}