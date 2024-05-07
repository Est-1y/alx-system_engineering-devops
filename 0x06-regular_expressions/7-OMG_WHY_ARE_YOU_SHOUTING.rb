#!/usr/bin/env ruby
# Ruby script containing regualar expression to match only Capital letters in a string of words.

puts ARGV[0].scan(/[A-Z]*/).join
