#!/bin/sh
echo "build duration ..."
g++ testDuration.cpp -o duration -std=c++11
echo "build system_clock ..."
g++ testSystemClock.cpp -o system_clock -std=c++11
echo "build steady_clock ..."
g++ testSteadyClock.cpp -o steady_clock -std=c++11
echo "build time_point ..."
g++ testTimePoint.cpp -o time_point -std=c++11