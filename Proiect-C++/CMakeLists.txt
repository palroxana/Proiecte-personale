cmake_minimum_required(VERSION 3.22)
project(sda)

set(CMAKE_CXX_STANDARD 14)

add_executable(sda main.cpp TAD/ABCNode.h TAD/ABC.h Domain/Util.h Domain/Util.cpp Service/ServiceUtil.cpp Service/ServiceUtil.h UI/UI.h UI/UI.cpp Service/ServicePri.cpp Service/ServicePri.h Domain/Mesaj.cpp Domain/Mesaj.h Service/Servicemes.cpp Service/Servicemes.h Repository/RepoFile.h Repository/RepoFile.cpp Domain/Prietenie.cpp Repository/RepoFilemes.cpp Repository/RepoFilemes.h Repository/RepoFilepri.cpp Repository/RepoFilepri.h)
