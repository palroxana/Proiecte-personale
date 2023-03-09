#pragma once
#include "../TAD/ABC.h"
#include"../Domain/Prietenie.h"
#include "../Repository/RepoFilepri.h"
class ServicePri{
private:
    RepoFilepri repopri;
public:
    ServicePri();
    explicit ServicePri(const RepoFilepri& repopri);
    void add(int id1,int id2);
    void ster(int id1, int id2);
    void stergeptutil(int id);
    vector<Pri> listapri();
};
