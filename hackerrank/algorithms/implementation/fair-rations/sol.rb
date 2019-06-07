def fairRations(b)
  breads = 0
  i = 0

  while i < b.length
    if b[i] % 2 != 0
      if i >= b.length - 1
        return "NO"
      end
      b[i] += 1
      b[i+1] += 1
      breads += 2  
    end

    i += 1
  end
  return breads 
end

res = fairRations([1,2])
puts res