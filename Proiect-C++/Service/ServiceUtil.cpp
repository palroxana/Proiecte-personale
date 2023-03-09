#include "../Service/ServiceUtil.h"
#include<iostream>
#include <utility>

using namespace std;

Serviceutil::Serviceutil() = default;

Serviceutil::Serviceutil(RepoFile &repo) {
    this->repo = repo;
}

void Serviceutil::add(int id, string nume, int varsta) {
    Util u(id, std::move(nume), varsta);
    repo.add(u);
    repo.save_to_file();
}
int Serviceutil::exista(const string& nume){
    vector<Util> util = repo.getAll();
    int size = 0;
    for (auto u: util) {
        if (nume== u.getnume()) {
            size++;
        }
    }
    if (size == 0) { return 0;}
    return 1;
}

Util Serviceutil::findutil(const string& nume) {
    vector<Util> util = repo.getAll();
    int size = 0;
    for (auto u: util) {
        if (nume==u.getnume()) {
            size++;
            cout << u.getid() << ' ' << u.getnume() << ' ' << u.getvarsta() << endl;
        }
    }
    if (size == 0) { cout << "Nu exista un utilizator";}
    else {
        cout << "Dintre utilizatorii de mai sus pe care vreti sa il alegeti?" << endl;
        cout << "Dati id-ul: " << endl;
        int id;
        cin >> id;
        for (const auto& u: util) {
            if (id == u.getid()) {
                return u;

            }
        }
    }
    return {};
}

Util Serviceutil::findutilptnume(const string &nume) {
    vector<Util> util = repo.getAll();
    for (auto u: util) {
        if (nume==u.getnume()) {
            return u;
        }
    }
    return {};
}

int Serviceutil::idunic(int id) {
    vector<Util> util=repo.getAll();
    for (const auto& u: util) {
        if (id==u.getid()) {
            return 0;
        }
    }
    return 1;
}
int Serviceutil::idnr(const string& id) {
    for (char i : id) {
        if(isdigit(i))
        {
            return 1;
        }
    }
    return 0;
}
Util Serviceutil::findutilptpri(int id) {
    vector<Util> util = repo.getAll();
    for (const auto& u: util) {
        if (id==u.getid()) {
            return u;}
    }
    return {};
}

void Serviceutil::update(const string& nume) {
    cout << "Dati noul id:" << endl;
    string idnou;
    int varstanou, idnounr;
    if(idnr(idnou)==0)
    {
        int ok1=1;
        while(ok1==1)
        {
            cout<<"id-ul trebuie sa fie un numar: ";
            cin>>idnou;
            if(idnr(idnou)==1)
            {
                ok1=0;
            }
        }
    }
    idnounr= stoi(idnou);
    if(idunic(idnounr)==0)
    {
        int ok=1;
        while(ok==1)
        {
            cout<<"Id-ul exista, dati alt id: ";
            cin>>idnounr;
            if(idunic(idnounr)==1)
            {
                ok=0;
            }
        }
    }
    cout << "Dati numele nou:" << endl;
    string numenou;
    cin >> ws;
    getline(cin,numenou);
    cout << "Dati varsta noua:" << endl;
    cin >> varstanou;
    Util un(idnounr, numenou, varstanou);
    Util temp = findutil(nume);
    repo.update(temp, un);
    repo.save_to_file();
}

void Serviceutil::remove(const string& nume) {
    Util temp = findutil(nume);
    repo.remove(temp);
    repo.save_to_file();
}

vector<Util> Serviceutil::getAll() {
    return repo.getAll();
}