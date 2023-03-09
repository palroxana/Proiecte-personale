#pragma once
#include <iostream>
using namespace std;

class Util {
private:
    int id{};
    string nume;
    int vasrta{};
public:
    Util();
    Util(int,string,int);
    Util(const Util&);
    int getid() const;
    string getnume();
    int getvarsta() const;
    void setid(int);
    void setnume(string);
    void setvarsta(int);

    Util& operator=(const Util&);
    bool operator==(const Util&);
    bool operator>(const Util&) const;
    bool operator<(const Util&) const;
    friend ostream& operator<<(ostream&, Util&);


};

