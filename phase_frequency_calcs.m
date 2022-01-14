
R = 10 % m
c= 3e8;
tau =  2*R/(c/1.8)

B = 200e6
T = 1; 

K = 2*pi*B/T

t = 0:0.01:1;

epsilon = 2.1;

omega_c = 2*pi*300

phi_d = omega_c * tau + K*tau*(t - T/2) - K*tau^2 /2



plot(t,phi_d)



f_d = 2*B*R*sqrt(epsilon)/c/T
