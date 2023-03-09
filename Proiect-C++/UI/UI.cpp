#include "../UI/UI.h"
#include <iostream>
#include<string>

using namespace std;

UI::UI() = default;

UI::UI(Serviceutil &service, Servicemes &servicemes, ServicePri &servicepri) {
    this->service = service;
    this->servicemes = servicemes;
    this->servicepri = servicepri;
}

void UI::adaugautil() {
    string id;
    int varsta, idnr1 = 0;
    string tempnume;
    cout << "Dati id:" << endl;
    cin >> id;
    if (Serviceutil::idnr(id) == 0) {
        int ok1 = 1;
        while (ok1 == 1) {
            cout << "id-ul trebuie sa fie un numar: ";
            cin >> id;
            if (Serviceutil::idnr(id) == 1) {
                ok1 = 0;
            }
        }
    }
    idnr1 = stoi(id);
    if (service.idunic(idnr1) == 0) {
        int ok = 1;
        while (ok == 1) {
            cout << "Id-ul exista, dati alt id: ";
            cin >> idnr1;
            if (service.idunic(idnr1) == 1) {
                ok = 0;
            }
        }
    }
    cout << "Dati nume:" << endl;
    cin >> ws;
    getline(cin, tempnume);
    cout << "Dati varsta:" << endl;
    cin >> varsta;
    this->service.add(idnr1, tempnume, varsta);
}

void UI::adaugames() {
    string util1;
    string util2;
    string tempmesaj;
    cout << "Dati numele utilizatorului care trimite un mesaj:" << endl;
    cin >> ws;
    getline(cin, util1);
    if (this->service.exista(util1) == 0) {
        cout << "Utilizatorul nu exista";
    } else {
        Util temp = this->service.findutil(util1);
        cout << "Dati numele utilizatorului care primeste un mesaj:" << endl;
        cin >> ws;
        getline(cin, util2);
        if (this->service.exista(util2) == 0) {
            cout << "Utilizatorul nu exista";

        } else {
            Util temp1 = this->service.findutil(util2);
            cout << "Dati mesajul";
            cin >> ws;
            getline(cin, tempmesaj);
            this->servicemes.add(temp, temp1, tempmesaj);
        }
    }


}

void UI::adaugapri() {
    string util1;
    string util2;
    string tempmesaj;
    cout << "Dati numele utilizatorului care trimite cerere:" << endl;
    cin >> ws;
    getline(cin, util1);
    if (this->service.exista(util1) == 0) {
        cout << "Utilizatorul nu exista";
    } else {
        Util temp = this->service.findutil(util1);
        cout << "Dati numele utilizatorului care primeste cerere:" << endl;
        cin >> ws;
        getline(cin, util2);
        if (this->service.exista(util2) == 0) {
            cout << "Utilizatorul nu exista";

        } else {
            Util temp1 = this->service.findutil(util2);
            this->servicepri.add(temp.getid(), temp1.getid());
        }
    }


}

void UI::afisareutil() {

    vector<Util> util = this->service.getAll();
    for (auto u: util) {
        cout << u.getid() << ' ' << u.getnume() << ' ' << u.getvarsta() << endl;
    }
}

void UI::afisaremes() {
    string util1;
    string util2;
    cout << "Dati numele primului utilizator:" << endl;
    cin >> ws;
    getline(cin, util1);
    if (this->service.exista(util1) == 0) {
        cout << "Utilizatorul nu exista";
    } else {
        Util temp = this->service.findutil(util1);
        cout << "Dati numele celuilalt utilizator:" << endl;
        cin >> ws;
        getline(cin, util2);
        if (this->service.exista(util2) == 0) {
            cout << "Utilizatorul nu exista";

        } else {
            Util temp1 = this->service.findutil(util2);
            this->servicemes.mesaje12(temp, temp1);
        }
    }
}

void UI::afispri() {
    cout << "Dati numele persoanei careia vreti sa ii vedeti lista de prieteni: ";
    string util;
    cin >> ws;
    getline(cin, util);
    if (this->service.exista(util) == 0) {
        cout << "Utilizatorul nu exista";
    } else {
        Util temp = this->service.findutil(util);
        int id = temp.getid();
        vector<Pri> pri = this->servicepri.listapri();
        for (auto &i: pri) {
            if (id == i.getid1()) {
                Util temp1 = this->service.findutilptpri(i.getid2());
                cout << temp1.getnume() << '\n';
            }
            if (id == i.getid2()) {
                Util temp1 = this->service.findutilptpri(i.getid1());
                cout << temp1.getnume() << '\n';
            }
        }
    }
}


void UI::sterutil() {
    string nume;
    cout << "Dati nume:" << endl;
    cin >> ws;
    getline(cin, nume);
    this->service.remove(nume);
}

void UI::stermes() {
    string util1;
    cout << "Dati numele utilizatorului de la care vreti sa stergeti mesaje:" << endl;
    cin >> ws;
    getline(cin, util1);
    if (this->service.exista(util1) == 0) {
        cout << "Utilizatorul nu exista";
    } else {
        Util temp = this->service.findutil(util1);
        this->servicemes.stergere(temp);
    }
}

void UI::sterpri() {
    string util1;
    string util2;
    cout << "Dati numele primului utilizatorului:" << endl;
    cin >> ws;
    getline(cin, util1);
    if (this->service.exista(util1) == 0) {
        cout << "Utilizatorul nu exista";
    } else {
        Util temp = this->service.findutil(util1);
        cout << "Dati numele celuilalt utilizator:" << endl;
        cin >> ws;
        getline(cin, util2);
        if (this->service.exista(util2) == 0) {
            cout << "Utilizatorul nu exista";

        } else {
            Util temp1 = this->service.findutil(util2);
            this->servicepri.ster(temp.getid(), temp1.getid());
        }
    }
}

void UI::updateutil() {
    string nume;
    cout << "Dati numele:" << endl;
    cin >> ws;
    getline(cin, nume);
    this->service.update(nume);
}

void UI::show_menu() {
    cout << "Meniu" << endl;
    cout << "1.Utilizator" << endl;
    cout << "2.Prietenie" << endl;
    cout << "3.Mesaje" << endl;
    cout << "0.Exit" << endl;
}

void menu_util() {
    cout << "Utilizatori" << endl;
    cout << "1.Adaugati util" << endl;
    cout << "2.Afisare util" << endl;
    cout << "3.Sterge util" << endl;
    cout << "4.Modificare util" << endl;
    cout << "0.Exit" << endl;
}

void UI::menu_mesaje() {
    cout << "Mesaje" << endl;
    cout << "1.Adaugati mesaj" << endl;
    cout << "2.Afisare mesaje dintre 2 util" << endl;
    cout << "3.Sterge mesaj" << endl;
    cout << "0.Exit" << endl;
}

void menu_pri() {
    cout << "Prieteni" << endl;
    cout << "1.Adaugati prieten" << endl;
    cout << "2.Afisare lista de prieteni" << endl;
    cout << "3.Sterge prieten" << endl;
    cout << "0.Exit" << endl;
}

void UI::run_pri() {
    int opt;
    while (true) {
        menu_pri();
        cout << "Dati optiunea:";
        cin >> opt;
        switch (opt) {
            case 1: {
                adaugapri();
                break;
            }
            case 2: {
                afispri();
                break;
            }
            case 3: {
                sterpri();
                break;
            }
            case 0: {
                return;
            }
            default:
                cout << "Op gresita" << endl;
        }

    }
}

void UI::run_mes() {
    int opt;
    while (true) {
        menu_mesaje();
        cout << "Dati optiunea:";
        cin >> opt;
        switch (opt) {
            case 1: {
                adaugames();
                break;
            }
            case 2: {
                afisaremes();
                break;
            }
            case 3: {
                stermes();
                break;
            }
            case 0: {
                return;
            }
            default:
                cout << "Op gresita" << endl;
        }

    }
}

void UI::run_util() {
    int opt;
    while (true) {
        menu_util();
        cout << "Dati optiunea:";
        cin >> opt;
        switch (opt) {
            case 1: {
                adaugautil();
                break;
            }
            case 2: {
                afisareutil();
                break;
            }
            case 3: {
                sterutil();
                break;
            }
            case 4: {
                updateutil();
                break;
            }
            case 0: {
                return;
            }
            default:
                cout << "Op gresita" << endl;
        }

    }
}

void UI::run_menu() {
    int opt;
    while (true) {
        show_menu();
        cout << "Dati optiunea:";
        cin >> opt;
        switch (opt) {
            case 1: {
                run_util();
                break;
            }
            case 2: {
                run_pri();
                break;
            }
            case 3: {
                run_mes();
                break;
            }
            case 0: {
                return;
            }
            default:
                cout << "Op gresita" << endl;
        }

    }
}


