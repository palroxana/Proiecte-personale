#include "../Service/Servicemes.h"
#include<iostream>
#include <utility>

using namespace std;

Servicemes::Servicemes() = default;

Servicemes::Servicemes(RepoFilemes &repomes) {
    this->repomes = repomes;
}

void Servicemes::add(const Util& util1, const Util& util2, string mesaj) {
    Mesaj m(util1,util2,std::move(mesaj));
    repomes.add(m);
    repomes.save_to_file();
}


void Servicemes::stergere(Util util1) {
    vector<Mesaj> mes = repomes.getAll();
    int size=0;
    for (auto m: mes) {
        if (util1== m.getutil1())
        {
            size++;
            cout<<size<<' ' <<m.getutil1().getnume() << ' ' << m.getutil2().getnume() << ' ' << m.getmesaj() << endl;
        }

    }
    cout << "Dintre mesajele de mai sus pe care vreti sa il stergeti?" << endl;
    cout << "Dati id-ul:" << endl;
    int id;
    cin >> id;
    for (auto m: mes) {
        if (util1== m.getutil1()) {
            if (id != 1)
                id--;
            else {
                repomes.remove(m);
                repomes.save_to_file();
            break;
            }
        }
    }

}
void Servicemes::mesaje12(Util util1, Util util2) {
    vector<Mesaj> mes = repomes.getAll();
    for (auto m: mes) {
        if (util1==m.getutil1()&&util2==m.getutil2())
            cout << m.getutil1().getnume() << ' ' << m.getmesaj() << endl;
        else{
            if(util1==m.getutil2()&&util2==m.getutil1())
                cout<< m.getutil1().getnume()<< ' '<<m.getmesaj()<<endl;
        }
    }

}