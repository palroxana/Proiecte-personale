#pragma once
#include "../TAD/List.h"

class RepoFile: public Lista<Util>{
private:
    const char* filename{};
public:
    RepoFile();
    explicit RepoFile(const char* filename);
    ~RepoFile();
    void clear_file();
    void save_to_file();
};
