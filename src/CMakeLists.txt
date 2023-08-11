set(CMAKE_CXX_STANDARD 20)
cmake_minimum_required(VERSION 3.2)
project(2E_EVRP)

enable_language(CXX)

list(APPEND CMAKE_MODULE_PATH ${PROJECT_SOURCE_DIR})
set(CMAKE_BUILD_TYPE "Release")

set(CMAKE_CXX_FLAGS "-O3")


set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -D __FILENAME__='\"$(subst  ${CMAKE_SOURCE_DIR}/,,$(abspath $<))\"'")



include_directories(INSTANCIA)
include_directories(K_MEANS)
include_directories(CONSTRUTIVO)
include_directories(BUSCA_LOCAL)


set(SOURCES
        INSTANCIA/Parametros.cpp
        INSTANCIA/Instance.cpp
        CONSTRUTIVO/Construtivo.cpp
        CONSTRUTIVO/Construtivo2.cpp
        CONSTRUTIVO/Construtivo3.cpp
        CONSTRUTIVO/Construtivo4.cpp
        BUSCA_LOCAL/LocalSearch.cpp
        BUSCA_LOCAL/LocalSearch2.cpp
        K_MEANS/k_means.cpp
        main.cpp
        Satelite.cpp
        Auxiliary.cpp
        Route.cpp
        Vnd.cpp
        ViabilizadorRotaEv.cpp
        Teste.cpp
        Solucao.cpp
        EvRoute.cpp
        mersenne-twister.cpp
        Constants.cpp
        Grasp.cpp
        PreProcessamento.cpp
        IG.cpp)



add_executable(run ${SOURCES})

target_link_libraries(run LINK_PUBLIC ${Boost_LIBRARIES})