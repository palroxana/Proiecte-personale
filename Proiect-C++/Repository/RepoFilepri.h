#pragma once
#include "../TAD/ABC.h"
#include "../Domain/Prietenie.h"
class RepoFilepri : public ABC<Pri>{
private:
    const char* filename{};
public:
    RepoFilepri();
    explicit RepoFilepri(const char* filename);
    ~RepoFilepri();
    void clear_file();
    void save_to_file();

};

