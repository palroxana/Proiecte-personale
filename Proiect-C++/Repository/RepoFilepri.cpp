
#include "RepoFilepri.h"
#include <fstream>
#include <vector>

using namespace std;

RepoFilepri::RepoFilepri() : ABC<Pri>() {

}

RepoFilepri::RepoFilepri(const char *filename) {
    this->filename = filename;
    fstream f;
    f.open(this->filename, fstream::in | fstream::out | fstream::app);
    if (f.is_open()) {
        int id;
        f >> id;
        while (!f.eof()) {
            int id1,id2;
            f>>id1;
            f>>id2;
            Pri p(id,id1,id2);
            RepoFilepri::add(p);
            f >> id;
        }
    }
    f.close();
}

RepoFilepri::~RepoFilepri() {
    fstream f(this->filename);
    if (f.is_open())
        f.close();
}

void RepoFilepri::save_to_file() {
    ofstream f;
    f.open(this->filename, ios::out);
    if (f.is_open()) {
        vector<Pri> pri = ABC<Pri>::getAll();
        for (auto &i: pri)
            f << i.getid()<<'\n'
            <<i.getid1()<<'\n'
            <<i.getid2()<<'\n';
        f.close();
    }
}

void RepoFilepri::clear_file() {
    ofstream f;
    f.open(this->filename, std::ofstream::out | std::ofstream::trunc);
    f.close();
}
