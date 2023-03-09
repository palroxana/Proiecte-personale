#pragma once
#include <iostream>
using namespace std;

class Pri {
private:
    int id{};
    int id1;
    int id2;
public:
    Pri();
    Pri(int,int,int);
    Pri(const Pri&);
    int getid() const;
    int getid1() const;
    int getid2() const;
    void setid(int);
    void setid1(int);
    void setid2(int);

    Pri& operator=(const Pri&);
    bool operator==(const Pri&) const;
    friend ostream& operator<<(ostream&, Pri&);
    bool operator>(const Pri&) const;
    bool operator<(const Pri&) const;


};

