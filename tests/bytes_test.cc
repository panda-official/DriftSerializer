// Copyright 2023 PANDA GmbH

#include <drift_bytes/bytes.h>

#include <limits>

#include <catch2/catch_test_macros.hpp>

#include "catch2/generators/catch_generators.hpp"

using drift_bytes::InputBuffer;
using drift_bytes::OutputBuffer;
using drift_bytes::Shape;
using drift_bytes::Type;
using drift_bytes::Variant;

TEST_CASE("Test") {
  Variant var1({1, 3}, {1, 2, 3});
  Variant var2 =
      GENERATE(Variant({2}, {true, false}), Variant({2}, {1.0, 2.0}),
               Variant({2}, {"Hello", "World"}), Variant({3}, {1l, 2l, 3l}),
               Variant({3}, {1ul, 2ul, 3ul}), Variant({3}, {1.0f, 2.0f, 3.0f}));

  OutputBuffer out;
  out.push_back(var1);
  out.push_back(var2);

  InputBuffer in(out.str());

  REQUIRE(in.pop() == var1);
  REQUIRE_FALSE(in.empty());

  REQUIRE(in.pop() == var2);
  REQUIRE(in.empty());
}
