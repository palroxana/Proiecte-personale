#pragma once
#include<iostream>
#include"Util.h"
using namespace std;
class Mesaj {
private:
    Util util1;
    Util util2;
    string mesaj{};
public:
    Mesaj();
    Mesaj(const Util&,const Util&,string);
    Mesaj(const Mesaj&);
    Util getutil1();
    Util getutil2();
    string getmesaj();
    void setutil1(const Util&);
    void setutil2(const Util&);
    void setmesaj(string);

    Mesaj& operator=(const Mesaj&);
    bool operator==(const Mesaj&);
    friend ostream& operator<<(ostream&, Mesaj&);

};

