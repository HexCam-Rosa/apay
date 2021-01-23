apay
====

## Building the Hello World project (Check CMake installed)

    mkdir build
    cd build
    cmake ..
    make

    # Now run it!
    ./src/apay

## Building GNURadio project

    Open GNURadio Companion, click "Execute flow graph"
    It will generate a folder called apay (we might change this later)
    cd apay
    cmake .
    make
    ./apay
    You should hear your voice echoed back to you!
