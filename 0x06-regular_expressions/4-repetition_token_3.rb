#!/usr/bin/env ruby
# Ruby script that match "hbn, hbtn, hbtttttn" and not "hbon"

puts ARGV[0].scan(/hbt*n/).join
