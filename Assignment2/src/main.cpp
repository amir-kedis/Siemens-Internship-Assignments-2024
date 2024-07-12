/* ===========================================================================
 *
 *
 *      ██╗███╗   ███╗ █████╗ ██╗███╗   ██╗██╗
 *     ██╔╝████╗ ████║██╔══██╗██║████╗  ██║╚██╗
 *    ██╔╝ ██╔████╔██║███████║██║██╔██╗ ██║ ╚██╗
 *    ╚██╗ ██║╚██╔╝██║██╔══██║██║██║╚██╗██║ ██╔╝
 *     ╚██╗██║ ╚═╝ ██║██║  ██║██║██║ ╚████║██╔╝
 *      ╚═╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝╚═╝
 *
 *      Author: Amir Kedis
 *
 *      Runs the packet tester and generates the CSV output file.
 *===========================================================================*/
#include "packet_tester.hpp"
#include <fstream>
#include <iostream>
#include <string>
#include <vector>

/**
 * Generates a CSV file with packet information.
 *
 * @param packets packet modules vector
 * @param results results out Yes or No
 * @param filename the filename to write the output to
 */
void geneateCSV(vector<int> &packets, vector<string> &results,
                string filename) {
  ofstream file(filename);

  file << "PacketID,MouduleNumber,ValidModule" << endl;
  for (size_t i = 0; i < packets.size(); ++i) {
    file << i + 1 << "," << packets[i] << "," << results[i] << endl;
  }

  file.close();
}

/**
 * Tests Packet Tester for a certain testcase
 */
int main() {
  int num_modules = 4;
  vector<int> packets = {1, 3, 4, 4, 1, 3};

  PacketTester pt(num_modules);
  vector<string> results;
  pt.validatePackets(packets, results);

  geneateCSV(packets, results, "output.csv");
  return 0;
}
