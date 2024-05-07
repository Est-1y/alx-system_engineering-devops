#!/usr/bin/env ruby
# Ruby script to match "hbtn, hbttn, hbtttn, hbttttn" and not "hbn"

puts ARGV[0].scan(/hbt+n/).join
