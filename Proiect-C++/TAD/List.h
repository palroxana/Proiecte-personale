#pragma once
#include <vector>
#include<bits/stdc++.h>
#include "../Domain/Util.h"

using namespace std;
template<class T>
class Lista {
private:
    vector<T> elems;
public:
    Lista()= default;
    void add(T& elem){
        elems.push_back(elem);
    }

    bool cautare(T& elem){
//        vector<T>::iterator it;
//        it = find(elems.begin(), elems.end(), elem);
        for(T& e:elems){
            if(e == elem) return true;
        }
        return false;
    }

    vector<T> getAll(){
        return elems;
    }

    int size(){
        return elems.size();
    }

    void remove(T& elem){
        for(int i = 0; i< elems.size(); i++){
            if(elem == elems[i]) elems[i] = elems[elems.size()-1];
        }
        elems.pop_back();
    }

    void update(T& vechi, T&nou){
        for(int i = 0; i<elems.size(); i++){
            if(vechi == elems[i]) elems[i] = nou;
        }
    }

};
