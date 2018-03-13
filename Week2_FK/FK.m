function T = FK(ss1,ss2,ss3,ss4,ss5,ss6,M,theta)

ex1=expm(ss1*deg2rad(theta(1)));
ex2=expm(ss2*deg2rad(theta(2)));
ex3=expm(ss3*deg2rad(theta(3)));
ex4=expm(ss4*deg2rad(theta(4)));
ex5=expm(ss5*deg2rad(theta(5)));
ex6=expm(ss6*deg2rad(theta(6)));

T = ex1*ex2*ex3*ex4*ex4*ex5*ex6*M;

end

