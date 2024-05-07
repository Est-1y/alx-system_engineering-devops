#!/usr/bin/env ruby
# Ruby script to match words/strings that start with `h` and end with `n`.
# disregarding whatever is in the middle or single character.

puts ARGV[0].scan(/h.n/).join
