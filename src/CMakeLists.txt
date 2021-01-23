cmake_minimum_required(VERSION 2.8)
project(apay)

# add_subdirectory(apay)
set(SOURCE_FILES main.cpp)

add_executable(apay ${SOURCE_FILES})
# install(TARGETS apay DESTINATION ${APAY_INSTALL_BIN_DIR})
