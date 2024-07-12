#include "../src/packet_tester.hpp"
#include "gtest/gtest.h"

TEST(PacketValidatorTest, SampleTestCase) {
  // Arrange
  int num_modules = 4;
  vector<int> packets = {1, 3, 4, 4};
  PacketTester pt(num_modules);

  // Act
  vector<string> results;
  pt.validatePackets(packets, results);

  // Assert
  vector<string> expected = {"Yes", "No", "Yes", "Yes"};
  ASSERT_EQ(results, expected) << "Mistake of output of sample testcase";
}

TEST(PacketValidatorTest, EdgeArroundNumOfModules) {
  // Arrange
  int num_modules = 4;
  vector<int> packets = {1, 3, 4, 4, 1, 2};
  PacketTester pt(num_modules);

  // Act
  vector<string> results;
  pt.validatePackets(packets, results);

  // Assert
  vector<string> expected = {"Yes", "No", "Yes", "Yes", "Yes", "Yes"};
  ASSERT_EQ(results, expected) << "Didn't handle edge correctly";
}

TEST(PacketValidatorTest, OnlyOnePacket) {
  // Arrange
  int num_modules = 4;
  vector<int> packets = {1};
  PacketTester pt(num_modules);

  // Act
  vector<string> results;
  pt.validatePackets(packets, results);

  // Assert
  vector<string> expected = {"Yes"};
  ASSERT_EQ(results, expected)
      << "Didn't handle the case of having 1 packet correctly";
}

TEST(PacketValidatorTest, sameValue) {
  // Arrange
  int num_modules = 4;
  vector<int> packets = {1, 1, 1, 1, 1};
  PacketTester pt(num_modules);

  // Act
  vector<string> results;
  pt.validatePackets(packets, results);

  // Assert
  vector<string> expected = {"Yes", "Yes", "Yes", "Yes", "Yes"};
  ASSERT_EQ(results, expected)
      << "Didn't handle inputs when they have the same value";
}

TEST(PacketValidatorTest, monotonicIncrease) {
  // Arrange
  int num_modules = 5;
  vector<int> packets = {1, 2, 3, 4, 5};
  PacketTester pt(num_modules);

  // Act
  vector<string> results;
  pt.validatePackets(packets, results);

  // Assert
  vector<string> expected = {"Yes", "Yes", "Yes", "Yes", "Yes"};
  ASSERT_EQ(results, expected)
      << "monotonic increase";
}

TEST(PacketValidatorTest, monotonicIncreaseExceedingModules) {
  // Arrange
  int num_modules = 4;
  vector<int> packets = {1, 2, 3, 4, 5};
  PacketTester pt(num_modules);

  // Act
  vector<string> results;
  pt.validatePackets(packets, results);

  // Assert
  vector<string> expected = {"Yes", "Yes", "Yes", "Yes", "No"};
  ASSERT_EQ(results, expected)
      << "monotonic increase exceeding num of modules";
}

TEST(PacketValidatorTest, monotonicDecrease) {
  // Arrange
  int num_modules = 4;
  vector<int> packets = {5, 4, 3, 2, 1};
  PacketTester pt(num_modules);

  // Act
  vector<string> results;
  pt.validatePackets(packets, results);

  // Assert
  vector<string> expected = {"Yes", "No", "No", "No", "No"};
  ASSERT_EQ(results, expected) << "monotonic decrease";
}

TEST(PacketValidatorTest, NegativeNumbers) {
  // Arrange
  int num_modules = 4;
  vector<int> packets = {-5, -4, -3, -2, -1};
  PacketTester pt(num_modules);

  // Act
  vector<string> results;
  
  // Assert
  ASSERT_ANY_THROW(pt.validatePackets(packets, results));
}

TEST(PacketValidatorTest, MixedPostiveNegative) {
  // Arrange
  int num_modules = 4;
  vector<int> packets = {-5, 4, 3, -2, -1};
  PacketTester pt(num_modules);

  // Act
  vector<string> results;
  
  // Assert
  ASSERT_ANY_THROW(pt.validatePackets(packets, results));
}

int main(int argc, char **argv) {
  ::testing::InitGoogleTest(&argc, argv);
  return RUN_ALL_TESTS();
}
