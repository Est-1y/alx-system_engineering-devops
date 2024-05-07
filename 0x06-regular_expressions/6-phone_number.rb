#!/usr/bin/env ruby
# Ruby script containing a regular expression that matches a 10 digit phone number.

puts ARGV[0].scan(/^\d{10}$/).join
