#!/usr/bin/env ruby
# Ruby script accepting one argument and pass it to regular expression matching method 'School'
puts ARGV[0].scan(/School/).join
