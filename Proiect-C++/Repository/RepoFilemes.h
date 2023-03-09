#pragma once
#include "../TAD/List.h"
#include "../Domain/Mesaj.h"
class RepoFilemes: public Lista<Mesaj>{
private:
    const char* filename{};
public:
    RepoFilemes();
    explicit RepoFilemes(const char* filename);
    ~RepoFilemes();
    void clear_file();
    void save_to_file();
};
