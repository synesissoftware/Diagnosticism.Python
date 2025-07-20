#! /usr/bin/env python3

from diagnosticism import DOOMGram

import unittest


class DOOMGram_tester(unittest.TestCase):

    def test_empty(self):

        dg = DOOMGram()

        self.assertEqual(0, dg.event_count())

        self.assertEqual(0, dg.total_event_time_ns())
        self.assertIsNone(dg.min_event_time_ns())
        self.assertIsNone(dg.max_event_time_ns())

        self.assertEqual(0, dg.num_events_in_1ns())
        self.assertEqual(0, dg.num_events_in_10ns())
        self.assertEqual(0, dg.num_events_in_100ns())
        self.assertEqual(0, dg.num_events_in_1us())
        self.assertEqual(0, dg.num_events_in_10us())
        self.assertEqual(0, dg.num_events_in_100us())
        self.assertEqual(0, dg.num_events_in_1ms())
        self.assertEqual(0, dg.num_events_in_10ms())
        self.assertEqual(0, dg.num_events_in_100ms())
        self.assertEqual(0, dg.num_events_in_1s())
        self.assertEqual(0, dg.num_events_in_10s())
        self.assertEqual(0, dg.num_events_ge_100s())

        self.assertEqual("____________", dg.to_strip())
        self.assertEqual("____________", str(dg))
        self.assertEqual("DOOMGram(event_count=0, total_event_time_ns=0, min_event_time_ns=None, max_event_time_ns=None, num_events_in_1ns=0, num_events_in_10ns=0, num_events_in_100ns=0, num_events_in_1us=0, num_events_in_10us=0, num_events_in_100us=0, num_events_in_1ms=0, num_events_in_10ms=0, num_events_in_100ms=0, num_events_in_1s=0, num_events_in_10s=0, num_events_ge_100s=0)", repr(dg))

    def test_single_timing_event(self):

        dg = DOOMGram()

        dg.push_event_time_ms(13)

        self.assertEqual(1, dg.event_count())

        self.assertEqual(13000000, dg.total_event_time_ns())
        self.assertEqual(13000000, dg.min_event_time_ns())
        self.assertEqual(13000000, dg.max_event_time_ns())

        self.assertEqual(0, dg.num_events_in_1ns())
        self.assertEqual(0, dg.num_events_in_10ns())
        self.assertEqual(0, dg.num_events_in_100ns())
        self.assertEqual(0, dg.num_events_in_1us())
        self.assertEqual(0, dg.num_events_in_10us())
        self.assertEqual(0, dg.num_events_in_100us())
        self.assertEqual(0, dg.num_events_in_1ms())
        self.assertEqual(1, dg.num_events_in_10ms())
        self.assertEqual(0, dg.num_events_in_100ms())
        self.assertEqual(0, dg.num_events_in_1s())
        self.assertEqual(0, dg.num_events_in_10s())
        self.assertEqual(0, dg.num_events_ge_100s())

        self.assertEqual("_______a____", dg.to_strip())
        self.assertEqual("_______a____", str(dg))

    def test_zero_time_events(self):

        dg = DOOMGram()

        dg.push_event_time_ns(0)
        dg.push_event_time_us(0)
        dg.push_event_time_ms(0)
        dg.push_event_time_s(0)

        self.assertEqual(4, dg.event_count())

        self.assertEqual(0, dg.total_event_time_ns())
        self.assertEqual(0, dg.min_event_time_ns())
        self.assertEqual(0, dg.max_event_time_ns())

        self.assertEqual(0, dg.num_events_in_1ns())
        self.assertEqual(0, dg.num_events_in_10ns())
        self.assertEqual(0, dg.num_events_in_100ns())
        self.assertEqual(0, dg.num_events_in_1us())
        self.assertEqual(0, dg.num_events_in_10us())
        self.assertEqual(0, dg.num_events_in_100us())
        self.assertEqual(0, dg.num_events_in_1ms())
        self.assertEqual(0, dg.num_events_in_10ms())
        self.assertEqual(0, dg.num_events_in_100ms())
        self.assertEqual(0, dg.num_events_in_1s())
        self.assertEqual(0, dg.num_events_in_10s())
        self.assertEqual(0, dg.num_events_ge_100s())

        self.assertEqual("____________", dg.to_strip())
        self.assertEqual("____________", str(dg))

    def test_uniform_spread_timings_1(self):

        dg = DOOMGram()

        dg.push_event_time_ns(    9)
        dg.push_event_time_ns(   80)
        dg.push_event_time_ns(  700)
        dg.push_event_time_us(    6)
        dg.push_event_time_us(   50)
        dg.push_event_time_us(  400)
        dg.push_event_time_ms(    3)
        dg.push_event_time_ms(   20)
        dg.push_event_time_ms(  100)
        dg.push_event_time_s(     9)
        dg.push_event_time_s(    80)
        dg.push_event_time_s(   700)


        self.assertEqual(12, dg.event_count())

        self.assertEqual(789123456789, dg.total_event_time_ns())
        self.assertEqual(9, dg.min_event_time_ns())
        self.assertEqual(700_000_000_000, dg.max_event_time_ns())

        self.assertEqual(1, dg.num_events_in_1ns())
        self.assertEqual(1, dg.num_events_in_10ns())
        self.assertEqual(1, dg.num_events_in_100ns())
        self.assertEqual(1, dg.num_events_in_1us())
        self.assertEqual(1, dg.num_events_in_10us())
        self.assertEqual(1, dg.num_events_in_100us())
        self.assertEqual(1, dg.num_events_in_1ms())
        self.assertEqual(1, dg.num_events_in_10ms())
        self.assertEqual(1, dg.num_events_in_100ms())
        self.assertEqual(1, dg.num_events_in_1s())
        self.assertEqual(1, dg.num_events_in_10s())
        self.assertEqual(1, dg.num_events_ge_100s())

        self.assertEqual("aaaaaaaaaaaa", dg.to_strip())
        self.assertEqual("aaaaaaaaaaaa", str(dg))

    def test_uniform_spread_timings_2(self):

        dg = DOOMGram()

        dg.push_event_time_ns(     9)
        dg.push_event_time_ns(    80)
        dg.push_event_time_ns(   700)
        dg.push_event_time_ns(  6000)
        dg.push_event_time_ns( 50000)
        dg.push_event_time_ns(400000)
        dg.push_event_time_ms(     3)
        dg.push_event_time_ms(    20)
        dg.push_event_time_ms(   100)
        dg.push_event_time_ms(  9000)
        dg.push_event_time_ms( 80000)
        dg.push_event_time_ms(700000)

        self.assertEqual(12, dg.event_count())

        self.assertEqual(789123456789, dg.total_event_time_ns())
        self.assertEqual(9, dg.min_event_time_ns())
        self.assertEqual(700_000_000_000, dg.max_event_time_ns())

        self.assertEqual(1, dg.num_events_in_1ns())
        self.assertEqual(1, dg.num_events_in_10ns())
        self.assertEqual(1, dg.num_events_in_100ns())
        self.assertEqual(1, dg.num_events_in_1us())
        self.assertEqual(1, dg.num_events_in_10us())
        self.assertEqual(1, dg.num_events_in_100us())
        self.assertEqual(1, dg.num_events_in_1ms())
        self.assertEqual(1, dg.num_events_in_10ms())
        self.assertEqual(1, dg.num_events_in_100ms())
        self.assertEqual(1, dg.num_events_in_1s())
        self.assertEqual(1, dg.num_events_in_10s())
        self.assertEqual(1, dg.num_events_ge_100s())

        self.assertEqual("aaaaaaaaaaaa", dg.to_strip())
        self.assertEqual("aaaaaaaaaaaa", str(dg))

    def test_uniform_spread_timings_3(self):

        dg = DOOMGram()

        dg.push_event_time_ns(            9)
        dg.push_event_time_ns(           80)
        dg.push_event_time_ns(          700)
        dg.push_event_time_ns(         6000)
        dg.push_event_time_ns(        50000)
        dg.push_event_time_ns(       400000)
        dg.push_event_time_ns(      3000000)
        dg.push_event_time_ns(     20000000)
        dg.push_event_time_ns(    100000000)
        dg.push_event_time_ns(   9000000000)
        dg.push_event_time_ns(  80000000000)
        dg.push_event_time_ns( 700000000000)

        self.assertEqual(12, dg.event_count())

        self.assertEqual(789123456789, dg.total_event_time_ns())
        self.assertEqual(9, dg.min_event_time_ns())
        self.assertEqual(700_000_000_000, dg.max_event_time_ns())

        self.assertEqual(1, dg.num_events_in_1ns())
        self.assertEqual(1, dg.num_events_in_10ns())
        self.assertEqual(1, dg.num_events_in_100ns())
        self.assertEqual(1, dg.num_events_in_1us())
        self.assertEqual(1, dg.num_events_in_10us())
        self.assertEqual(1, dg.num_events_in_100us())
        self.assertEqual(1, dg.num_events_in_1ms())
        self.assertEqual(1, dg.num_events_in_10ms())
        self.assertEqual(1, dg.num_events_in_100ms())
        self.assertEqual(1, dg.num_events_in_1s())
        self.assertEqual(1, dg.num_events_in_10s())
        self.assertEqual(1, dg.num_events_ge_100s())

        self.assertEqual("aaaaaaaaaaaa", dg.to_strip())
        self.assertEqual("aaaaaaaaaaaa", str(dg))

    def test_uniform_spread_timings_4(self):

        dg = DOOMGram()

        dg.push_event_time_us(         6)
        dg.push_event_time_us(        50)
        dg.push_event_time_us(       400)
        dg.push_event_time_us(      3000)
        dg.push_event_time_us(     20000)
        dg.push_event_time_us(    100000)
        dg.push_event_time_us(   9000000)
        dg.push_event_time_us(  80000000)
        dg.push_event_time_us( 700000000)

        self.assertEqual(9, dg.event_count())

        self.assertEqual(789123456000, dg.total_event_time_ns())
        self.assertEqual(6_000, dg.min_event_time_ns())
        self.assertEqual(700_000_000_000, dg.max_event_time_ns())

        self.assertEqual(0, dg.num_events_in_1ns())
        self.assertEqual(0, dg.num_events_in_10ns())
        self.assertEqual(0, dg.num_events_in_100ns())
        self.assertEqual(1, dg.num_events_in_1us())
        self.assertEqual(1, dg.num_events_in_10us())
        self.assertEqual(1, dg.num_events_in_100us())
        self.assertEqual(1, dg.num_events_in_1ms())
        self.assertEqual(1, dg.num_events_in_10ms())
        self.assertEqual(1, dg.num_events_in_100ms())
        self.assertEqual(1, dg.num_events_in_1s())
        self.assertEqual(1, dg.num_events_in_10s())
        self.assertEqual(1, dg.num_events_ge_100s())

        self.assertEqual("___aaaaaaaaa", dg.to_strip())
        self.assertEqual("___aaaaaaaaa", str(dg))

    def test_several_distinct_timings(self):

        dg = DOOMGram()

        dg.push_event_time_ns(  23)
        dg.push_event_time_ns(  10)
        dg.push_event_time_us(   7)
        dg.push_event_time_us(   7)
        dg.push_event_time_us(  89)
        dg.push_event_time_ms( 248)
        dg.push_event_time_s(    5)
        dg.push_event_time_s(  309)

        self.assertEqual(8, dg.event_count())

        self.assertEqual(314248103033, dg.total_event_time_ns())
        self.assertEqual(10, dg.min_event_time_ns())
        self.assertEqual(309_000_000_000, dg.max_event_time_ns())

        self.assertEqual(0, dg.num_events_in_1ns())
        self.assertEqual(2, dg.num_events_in_10ns())
        self.assertEqual(0, dg.num_events_in_100ns())
        self.assertEqual(2, dg.num_events_in_1us())
        self.assertEqual(1, dg.num_events_in_10us())
        self.assertEqual(0, dg.num_events_in_100us())
        self.assertEqual(0, dg.num_events_in_1ms())
        self.assertEqual(0, dg.num_events_in_10ms())
        self.assertEqual(1, dg.num_events_in_100ms())
        self.assertEqual(1, dg.num_events_in_1s())
        self.assertEqual(0, dg.num_events_in_10s())
        self.assertEqual(1, dg.num_events_ge_100s())

        self.assertEqual("_a_aa___aa_a", dg.to_strip())
        self.assertEqual("_a_aa___aa_a", str(dg))

    def test_several_intersecting_timings(self):

        dg = DOOMGram()

        dg.push_event_time_ns(   11)
        dg.push_event_time_ns(   19)
        dg.push_event_time_ns(   19)
        dg.push_event_time_us(    7)
        dg.push_event_time_us(    7)
        dg.push_event_time_us(   89)
        dg.push_event_time_ms(  248)
        dg.push_event_time_ms(4_321)
        dg.push_event_time_s(     5)
        dg.push_event_time_s(   309)

        self.assertEqual(10, dg.event_count())

        self.assertEqual(318569103049, dg.total_event_time_ns())
        self.assertEqual(11, dg.min_event_time_ns())
        self.assertEqual(309_000_000_000, dg.max_event_time_ns())

        self.assertEqual(0, dg.num_events_in_1ns())
        self.assertEqual(3, dg.num_events_in_10ns())
        self.assertEqual(0, dg.num_events_in_100ns())
        self.assertEqual(2, dg.num_events_in_1us())
        self.assertEqual(1, dg.num_events_in_10us())
        self.assertEqual(0, dg.num_events_in_100us())
        self.assertEqual(0, dg.num_events_in_1ms())
        self.assertEqual(0, dg.num_events_in_10ms())
        self.assertEqual(1, dg.num_events_in_100ms())
        self.assertEqual(2, dg.num_events_in_1s())
        self.assertEqual(0, dg.num_events_in_10s())
        self.assertEqual(1, dg.num_events_ge_100s())

        self.assertEqual("_a_aa___aa_a", dg.to_strip())
        self.assertEqual("_a_aa___aa_a", str(dg))

    def test_many_cumulative_timings(self):

        dg = DOOMGram()

        [dg.push_event_time_ns(1) for _ in range(0,10000)]

        [dg.push_event_time_us(1) for _ in range(0,1000)]

        [dg.push_event_time_ms(1) for _ in range(0,100)]

        [dg.push_event_time_s(1) for _ in range(0,10)]

        self.assertEqual(11110, dg.event_count())

        self.assertEqual(10101010000, dg.total_event_time_ns())
        self.assertEqual(1, dg.min_event_time_ns())
        self.assertEqual(1_000_000_000, dg.max_event_time_ns())

        self.assertEqual(10_000, dg.num_events_in_1ns())
        self.assertEqual(0, dg.num_events_in_10ns())
        self.assertEqual(0, dg.num_events_in_100ns())
        self.assertEqual(1_000, dg.num_events_in_1us())
        self.assertEqual(0, dg.num_events_in_10us())
        self.assertEqual(0, dg.num_events_in_100us())
        self.assertEqual(100, dg.num_events_in_1ms())
        self.assertEqual(0, dg.num_events_in_10ms())
        self.assertEqual(0, dg.num_events_in_100ms())
        self.assertEqual(10, dg.num_events_in_1s())
        self.assertEqual(0, dg.num_events_in_10s())
        self.assertEqual(0, dg.num_events_ge_100s())

        self.assertEqual("e__d__c__b__", dg.to_strip())
        self.assertEqual("e__d__c__b__", str(dg))
        self.assertEqual("*--d--c--b--", dg.to_strip(range='abcd', zero='-'))
        self.assertEqual("#  #  c  b  ", dg.to_strip(range='abc', zero=' ', overflow='#'))
        self.assertEqual("DOOMGram(event_count=11110, total_event_time_ns=10101010000, min_event_time_ns=1, max_event_time_ns=1000000000, num_events_in_1ns=10000, num_events_in_10ns=0, num_events_in_100ns=0, num_events_in_1us=1000, num_events_in_10us=0, num_events_in_100us=0, num_events_in_1ms=100, num_events_in_10ms=0, num_events_in_100ms=0, num_events_in_1s=10, num_events_in_10s=0, num_events_ge_100s=0)", repr(dg))


# ############################## end of file ############################# #

