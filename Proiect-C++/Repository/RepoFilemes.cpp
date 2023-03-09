#include "RepoFilemes.h"
#include <iostream>
#include <fstream>

using namespace std;

RepoFilemes::RepoFilemes() : Lista<Mesaj>() {

}

RepoFilemes::RepoFilemes(const char *filename) {
    this->filename = filename;
    fstream f;
    f.open(this->filename, fstream::in | fstream::out | fstream::app);
    if (f.is_open()) {
        int id1;
        f >> id1;
        while (!f.eof()) {
            string nume1;
            int v1;
            int id2;
            string nume2;
            int v2;
            string mesaj;
            f>>ws;
            getline(f,nume1);
            f>>v1;
            f>>id2;
            f>>ws;
            getline(f, nume2);
            f>>v2;
            f>>ws;
            getline(f,mesaj);
            Util u1(id1,nume1,v1);
            Util u2(id2,nume2,v2);
            Mesaj m(u1, u2, mesaj);
            Lista<Mesaj>::add(m);
            f >> id1;
        }
    }
    f.close();
}

RepoFilemes::~RepoFilemes() {
    fstream f(this->filename);
    if (f.is_open())
        f.close();
}

void RepoFilemes::save_to_file() {
    ofstream f;
    f.open(this->filename, ios::out);
    if (f.is_open()) {
        vector<Mesaj> mes = RepoFilemes::getAll();
        for (auto &i: mes)
        {
            Util util1=i.getutil1();
            Util util2=i.getutil2();
            f << util1.getid() << '\n'
              << util1.getnume() << '\n'
              << util1.getvarsta() << '\n'
              << util2.getid() << '\n'
              << util2.getnume() << '\n'
              << util2.getvarsta() << '\n'
              <<i.getmesaj()<<'\n';
        }

        f.close();
    }
}
void RepoFilemes::clear_file() {
    ofstream f;
    f.open(this->filename, std::ofstream::out | std::ofstream::trunc);
    f.close();
}