cmake_minimum_required(VERSION 3.10)

project(PacketTester)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED True)

enable_testing()

include(FetchContent)

FetchContent_Declare(
  googletest
  URL https://github.com/google/googletest/archive/release-1.12.1.tar.gz
)

# For Windows: Prevent overriding the parent project's compiler/linker settings
set(gtest_force_shared_crt ON CACHE BOOL "" FORCE)
FetchContent_MakeAvailable(googletest)


set(SOURCES
    src/main.cpp
    src/packet_tester.cpp
)

set(HEADERS
    src/packet_tester.hpp
)

add_executable(PacketTester ${SOURCES} ${HEADERS})

add_executable(PacketTesterTests src/packet_tester.hpp src/packet_tester.cpp tests/test_packettester.cpp)

target_link_libraries(PacketTesterTests gtest gtest_main)

include(GoogleTest)
gtest_discover_tests(PacketTesterTests )

