#pragma once
#include "../Service/ServiceUtil.h"
#include "../Service/Servicemes.h"
#include"../Service/ServicePri.h"

class UI {
private:
    Serviceutil service;
    Servicemes servicemes;
    ServicePri servicepri;
    void adaugautil();
    void afisareutil();
    void sterutil();
    void updateutil();
    void adaugames();
    void afisaremes();
    void stermes();
    void adaugapri();
    void afispri();
    void sterpri();
public:
    UI();
    UI(Serviceutil&service,Servicemes &servicemes,ServicePri &servicepri);
    static void show_menu();
    void run_util();
    void run_mes();
    void run_pri();
    void run_menu();

    static void menu_mesaje();
};

