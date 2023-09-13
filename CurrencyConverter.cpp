#include <iostream>
#include <string>
#include <algorithm>  // Include for std::transform
#include <cctype>     // Include for std::tolower
#include <vector> 


using namespace std; 

int main(){
string yen = "Yen"; 
string yuan = "Yuan"; 
string cd = "Canadian Dollar"; 
string pound = "Pound"; 
double usd;   
cout<< "Welcome to the simple currency converter app \n Where you can convert USD to a currency of your choice \n"; 
while(usd != -1){
cout <<"Enter your USD amount below or enter -1 to exit!"<<endl; 
cin >> usd; 
if(usd == -1){
     break; }
cout <<"Great! Now what would you like to convert to? The options are listed below: \n-Yen\n-Pound\n-Canadian Dollar\n-Yuan\n"; 
string convertTo; 
cin >> convertTo; 

if(convertTo == yen){
    cout<<"The Yen equivalent of "<<usd<<" US dollars is "<<(usd*147.31)<<endl; 
}

else if(convertTo == yuan){
     cout<<"The Yuan equivalent of "<<usd<<" US dollars is "<<(usd*7.29)<<endl;  
}

else if(convertTo == cd){
     cout<<"The Canadian Dollar equivalent of "<<usd<<" US dollars is "<<(usd*1.36)<<endl;; 
}

else if(convertTo == pound){
     cout<<"The Pound equivalent of "<<usd<<" US dollars is "<<(usd*.8)<<endl; 
}

else{
    cout<<"Please enter one of the currencies listed above, make sure you spellcheck\n"; 
}
}
cout <<"Thank you come again!"; 
} 