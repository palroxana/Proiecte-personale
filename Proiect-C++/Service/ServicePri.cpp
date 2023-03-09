#include "ServicePri.h"
#include <random>
ServicePri::ServicePri() = default;

ServicePri::ServicePri(const RepoFilepri &repopri) {
    this->repopri = repopri;
}

void ServicePri::add(int id1, int id2) {
    vector<Pri> pri = repopri.getAll();
    int ok = 0;
    for (auto &i: pri) {
        if (id1 == i.getid1() && id2 == i.getid2()) {
            ok = 1;
            cout << "Relatia exista deja" << endl;
        }
        if (id1 == i.getid2() && id2 == i.getid1()) {
            ok = 1;
            cout << "Relatia exista deja" << endl;
        }
    }
    if (ok == 0) {
        int id;
        random_device randomDevice;
        uniform_int_distribution<int> intDistribution(1,1000);
        id=intDistribution(randomDevice);
        for(auto& i:pri)
        {
            while(id==i.getid()){
                id=intDistribution(randomDevice);
            }
        }
        Pri p(id, id1, id2);
        repopri.add(p);
        repopri.save_to_file();
    }
}

void ServicePri::ster(int id1, int id2) {
    vector<Pri> pri = repopri.getAll();
    int id = -1;
    for (auto &i: pri) {
        if (id1 == i.getid1() && id2 == i.getid2()) {
            id = i.getid();
        }
        if (id1 == i.getid2() && id2 == i.getid1()) {
            id = i.getid();
        }
    }
    if (id != -1) {
        Pri p(id, id1, id2);
        repopri.del(p);
        repopri.save_to_file();
    } else { cout << "Nu exista prietenie" << endl; }
}

vector<Pri> ServicePri::listapri() {
    vector<Pri> pri = repopri.getAll();
    return pri;
}

void ServicePri::stergeptutil(int id) {
    vector<Pri> pri = repopri.getAll();
    for (auto &i: pri) {
        if (id == i.getid1() || id == i.getid2()) {
            repopri.del(i);
            repopri.save_to_file();
        }

    }
}