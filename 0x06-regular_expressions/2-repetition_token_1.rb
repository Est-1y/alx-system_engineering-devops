#!/usr/bin/env ruby
# Ruby script to match "htn", "hbtn" and not "hbbtn" and or others

puts ARGV[0].scan(/hb?tn/).join
