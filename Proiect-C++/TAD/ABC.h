#pragma once

#include<vector>
#include "ABCNode.h"
#include<iostream>

template<class T>
class ABC {
protected:
    ABCNode<T> *root;

    void addItem(ABCNode<T> *ad, T elem) {

        if (ad->info > elem) { // adaugam pe stanga
            if (ad->left != nullptr) {
                addItem(ad->left, elem);
            } else {
                ad->left = new ABCNode<T>(elem, nullptr, nullptr);
            }
        } else {  //adaugam in dreapta
            if (ad->right != nullptr) {
                addItem(ad->right, elem);
            } else {
                ad->right = new ABCNode<T>(elem, nullptr, nullptr);
            }
        }
    }


    ABCNode<T>* minnod(ABCNode<T>* node) {
        ABCNode<T> *curent = node;
        while (curent->left != nullptr)
            curent = curent->left;
        return curent;
    }

    ABCNode<T>* del(ABCNode<T>* &r, T inf) {
        if (r == nullptr)
            return r;
        if (inf < r->info)
            r->left = del(r->left, inf);
        else if (inf > r->info)
            r->right = del(r->right, inf);
        else {
            if (r->left == nullptr && r->right == nullptr) {
                delete r;
                r = nullptr;
                return r;
            } else if (r->left == nullptr) {
                ABCNode<T>* t = r->right;
                delete r;
                r = t;
                return r;
            } else if (r->right == nullptr) {
                ABCNode<T>* t = r->left;
                delete r;
                r = t;
                return r;
            }
            ABCNode<T> *t = minnod(r->right);
            r->info = t->info;
            r->right = del(r->right, t->info);
        }
        return r;
    }


    void afisareIN(ABCNode<T> *ad) {
        if (ad != nullptr) {
                afisareIN(ad->left);
                cout << ad->info << endl;
                afisareIN(ad->right);
        }
    }
    void vec(ABCNode<T> *ad, vector<T> &vect) {
        if (ad != nullptr) {
            vec(ad->left, vect);
            vect.push_back(ad->info);
            vec(ad->right, vect);
        }
    }

public:
    ABC() { this->root = nullptr; }

    void add(T elem) {
        if (this->root == nullptr) this->root = new ABCNode<T>(elem, nullptr, nullptr);
        else addItem(this->root, elem);
    }

    void del(T elem) {
        del(root, elem);

    }

    void afisare() {
        afisareIN(this->root);
    }

    vector<T> getAll() {
        vector<T> all;
        vec(root,all);
        return all;
    }

};
