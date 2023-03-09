
#include"UI/UI.h"
#include "Domain/Util.h"
#include "Service/ServiceUtil.h"
#include "Service/Servicemes.h"
#include"Repository/RepoFile.h"
#include"Repository/RepoFilemes.h"
#include "Repository/RepoFilepri.h"
int main() {
    RepoFile repoF(R"(C:\Users\roxan\OneDrive\Desktop\sda\util.txt)");
    RepoFilemes repomes (R"(C:\Users\roxan\OneDrive\Desktop\sda\mes.txt)");
    RepoFilepri repopri(R"(C:\Users\roxan\OneDrive\Desktop\sda\pri.txt)");
    Lista<Util> repo;
    Serviceutil service(repoF);
    Servicemes servicemes(repomes);
    ServicePri servicepri(repopri);
    UI ui(service,servicemes,servicepri);
    ui.run_menu();


    return 0;
}
