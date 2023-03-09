#pragma once
#include "../TAD/List.h"
#include"../Domain/Util.h"
#include "../Repository/RepoFile.h"
class Serviceutil{
private:
    RepoFile repo;
public:
    Serviceutil();
    explicit Serviceutil(RepoFile&);
    void add(int, string, int);
    void update(const string&);
    void remove( const string&);
    int exista(const string&);
    Util findutil(const string&);
    Util findutilptpri(int id);
    Util findutilptnume(const string&);
    int idunic(int );
    static int idnr(const string&);
    vector<Util> getAll();
};
