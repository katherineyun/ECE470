function s = skew_4(a,q)
as = [0 -a(3) a(2); a(3) 0 -a(1); -a(2) a(1) 0];
s = [a; -as*q];
end


