#include <iostream>
 
using namespace std;
int n,i,c;
float a,b,h,s1,s2,stt;
float f(float x) // definir funcion a integrar
{
return x;
}
 int main(int argc, char* argv[])
 {

cout <<"Ingrese los valores par a, para b y para n" << endl;
cout <<"tome en cuenta que n debe ser un multiplo de 3" << endl;
cout << "a=" <<endl;
cin >> a; 
cout << "b=" <<endl;
cin >> b; 
cout << "n=" <<endl;
cin >> n;
h=(b-a)/n;
i=0;
s2=0;


for (i=1;i<n-1;i++)
{
    c= i%3;
	if (c=0)
	  s1=s1+2*f(a+i*h);
	else
	  s2=s2+3*f(a+i*h);
}
stt=(((3*h)/8)*(f(a)+s1+s2+f(b)));
cout<<"S1:"<<s1<< endl;
cout<<"S2:"<<s2<< endl;
cout<<"El area es:"<<stt<< endl;

	
system("pause"); 	
 	return 0;
 }
