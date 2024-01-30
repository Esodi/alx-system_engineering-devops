#!/usr/bin/env ruby
puts ARGV[0].scan(/\bfrom:\s*(\+?\d{11}|[A-Z][a-z]*\b)/).join + "," + ARGV[0].scan(/\bto:\s*(\+?\d{11}|[A-Z][a-z]*\b)/).join + "," + ARGV[0].scan(/\bflags:\s*(.?\d:.?\d:.?\d:.?\d:.?\d\b)/).join
