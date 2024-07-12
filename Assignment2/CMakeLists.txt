cmake_minimum_required(VERSION 3.10)

project(PacketTester)

set(CMAKE_CXX_STANDARD 11)

set(SOURCES
    src/main.cpp
    src/packet_tester.cpp
)

set(HEADERS
    src/packet_tester.hpp
)

add_executable(PacketTester ${SOURCES} ${HEADERS})

