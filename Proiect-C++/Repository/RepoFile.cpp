#include "RepoFile.h"
#include <iostream>
#include <fstream>
using namespace std;

RepoFile::RepoFile() : Lista<Util>() {

}

RepoFile::RepoFile(const char *filename) {
    this->filename = filename;
    fstream f;
    f.open(this->filename, fstream::in | fstream::out | fstream::app);
    if (f.is_open()) {
        int id;
        f >> id;
        while (!f.eof()) {
            string tempnume;
            int varsta;
            f>>ws;
            getline(f, tempnume);
            f >> varsta;
            Util ca(id, tempnume, varsta);
            RepoFile::add(ca);
            f >> id;
        }
    }
    f.close();
}

RepoFile::~RepoFile() {
    fstream f(this->filename);
    if (f.is_open())
        f.close();
}

void RepoFile::save_to_file() {
    ofstream f;
    f.open(this->filename, ios::out);
    if (f.is_open()) {
        vector<Util> util = RepoFile::getAll();
        for (auto &i: util)
            f << i.getid() << '\n'
              << i.getnume() << '\n'
              << i.getvarsta() << '\n';
        f.close();
    }
}
void RepoFile::clear_file() {
    ofstream f;
    f.open(this->filename, std::ofstream::out | std::ofstream::trunc);
    f.close();
}