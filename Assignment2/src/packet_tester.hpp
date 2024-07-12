/* ===========================================================================
 *
 *
 *    ██████╗  █████╗  ██████╗██╗  ██╗███████╗████████╗
 *    ██╔══██╗██╔══██╗██╔════╝██║ ██╔╝██╔════╝╚══██╔══╝
 *    ██████╔╝███████║██║     █████╔╝ █████╗     ██║
 *    ██╔═══╝ ██╔══██║██║     ██╔═██╗ ██╔══╝     ██║
 *    ██║     ██║  ██║╚██████╗██║  ██╗███████╗   ██║
 *    ╚═╝     ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝   ╚═╝
 *
 *    ████████╗███████╗███████╗████████╗███████╗██████╗ ██╗ ██╗
 *    ╚══██╔══╝██╔════╝██╔════╝╚══██╔══╝██╔════╝██╔══██╗╚██╗╚██╗
 *       ██║   █████╗  ███████╗   ██║   █████╗  ██████╔╝ ╚██╗╚██╗
 *       ██║   ██╔══╝  ╚════██║   ██║   ██╔══╝  ██╔══██╗ ██╔╝██╔╝
 *       ██║   ███████╗███████║   ██║   ███████╗██║  ██║██╔╝██╔╝
 *       ╚═╝   ╚══════╝╚══════╝   ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝ ╚═╝
 *
 *
 *      PackerTester Module checks if a certain packet configuration is valid.
 *
 *
 *===========================================================================*/

#ifndef PACKET_TESTER_H
#define PACKET_TESTER_H

#include <string>
#include <vector>

using namespace std;

/**
 * @brief A class to test the validity of packet sequences based on module
 * numbers.
 */
class PacketTester {

public:
  /*
   * @brief Constructs a PacketTester with a certain num_modules
   *
   * @param num_modules the maximum number after which counting should start
   * from 1
   */
  PacketTester(int num_modules);

  /*
   * @brief checks if 2 adjacent packets are valid or not
   *
   * @param current_module the module of a certain packet under check
   * @param next_module the module of another certain packet under check
   *
   * @throws ValueError if a packet module is negative number
   */
  bool isValidPacket(int current_module, int next_module);

  /*
   * @brief checks if the whole sequence of packet modules is correct
   *
   * @param packets the packet modules
   * @param results (out) the output for every packet either Yes or No
   */
  void validatePackets(const vector<int> &packets, vector<string> &results);

private:
  int num_modules;
};

#endif // PACKET_TESTER_H
