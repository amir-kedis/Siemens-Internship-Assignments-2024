#include "packet_tester.hpp"

PacketTester::PacketTester(int num_modules) : num_modules(num_modules) {}

bool PacketTester::isValidPacket(int current_module, int next_module) {
  if (current_module < 0 || next_module < 0)
    throw "Value Error";
  if (current_module == num_modules)
    return (next_module == num_modules || next_module == 1);
  else
    return (next_module == current_module || next_module == current_module + 1);
}

void PacketTester::validatePackets(const vector<int> &packets,
                                   vector<string> &results) {
  results.push_back("Yes");
  for (int i = 1; i < packets.size(); ++i)
    results.push_back(isValidPacket(packets[i - 1], packets[i]) ? "Yes" : "No");
}
