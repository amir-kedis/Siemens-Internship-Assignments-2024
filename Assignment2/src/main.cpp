#include "packet_tester.hpp"
#include <fstream>
#include <iostream>
#include <string>
#include <vector>

void geneateCSV(vector<int> &packets, vector<string> &results,
                string filename) {
  ofstream file(filename);

  file << "PacketID,MouduleNumber,ValidModule" << endl;
  for (size_t i = 0; i < packets.size(); ++i) {
    file << i + 1 << "," << packets[i] << "," << results[i] << endl;
  }

  file.close();
}

int main() {
  int num_modules = 4;
  vector<int> packets = {1, 3, 4, 4, 1, 3};

  PacketTester pt(num_modules);
  vector<string> results;
  pt.validatePackets(packets, results);

  geneateCSV(packets, results, "output.csv");
  return 0;
}
