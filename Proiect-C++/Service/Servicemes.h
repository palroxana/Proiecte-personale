#pragma once
#include "../TAD/List.h"
#include"../Domain/Mesaj.h"
#include"../Repository/RepoFilemes.h"

class Servicemes{
private:
    RepoFilemes repomes;
public:
    Servicemes();
    explicit Servicemes(RepoFilemes&);
    void add(const Util& util1, const Util& util2, string);
    void stergere(Util util1);
    void mesaje12(Util util1, Util util2);

};
