#ifndef PACKET_TESTER_H
#define PACKET_TESTER_H

#include <vector>
#include <string>

using namespace std;

class PacketTester {
public:
    PacketTester(int num_modules);

    bool isValidPacket(int current_module, int next_module);
    void validatePackets(const vector<int>& packets, vector<string>& results);

private:
    int num_modules;
};

#endif // PACKET_TESTER_H
