cmake_minimum_required(VERSION 2.8)

project(apay)

set(CMAKE_CXX_STANDARD 11)
# set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11 -O3")

set(CMAKE_INSTALL_PREFIX ${PROJECT_SOURCE_DIR})

# set(APAY_INSTALL_INCLUDE_DIR ${PROJECT_SOURCE_DIR}/include)
# set(APAY_INSTALL_BIN_DIR ${PROJECT_SOURCE_DIR}/bin)
# set(APAY_INSTALL_LIB_DIR ${PROJECT_SOURCE_DIR}/lib)

# set(APAY_HEADERS_DIR ${PROJECT_SOURCE_DIR}/src/apay)

add_subdirectory(src)
# add_subdirectory(test)
