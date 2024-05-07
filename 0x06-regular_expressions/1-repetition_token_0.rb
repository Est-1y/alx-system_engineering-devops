#!/usr/bin/env ruby
# Ruby script that matches "hbttn, hbtttn, hbttttn, hbtttttn"

puts ARGV[0].scan(/hbt{2,5}n/).join
