# Faulhaber
Little python script that shows coefficients of Faulhaber's polynomials.

# How to use it ?
You need python 2.7. Just run polymat.py in its folder and open res.html in a browser.

# Description
Faulhaber's polynomials are compact forms of the sum of the powers of the nth first integers.
Examples : 
power 0 : 1 + 1 + 1 + ... + 1 = n
power 1 : 1 + 2 + 3 + ... + n = n(n+1)/2
power 2 : 1 + 4 + 9 + ... + n^2 = n(n+1)(2n+1)/6

We can easely find a recursive formula to get the polynomial of power n+1 from polynomials of power
1 to n. We use it in this python script to compute Faulhaber's polynomials as far as we want.

# Output format
Running this script will update the res.html file. Opening it in a browser will show a table.
The nth line of the table represents the coeficients of the Faulbhaber polynomials of power n,
in increasing order of power (n starting at 0).
Example :
power 1 : n(n+1)/2 = 0 + (1/2)n + (1/2)n^2
thus on the line number 1 we have 0 ; 1/2 ; 1/2

# Licence
You're free to copy and use this code the way you want.
I haven't written the fraction API.

# Author
Emmanuel aka Exifers
