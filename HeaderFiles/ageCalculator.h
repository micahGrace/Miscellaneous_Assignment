#include<iostream>

//declaration
int ageCalculator();


//Definition goes here
int ageCalculator(){

	system("Enter your age");
	int current_year,age,birth_year;

	std::cout<<"Enter your Birth Year: \n";
	std::cin>> birth_year;

	std::cout<<"Enter the current year\n";
	std::cin>> current_year;
	
	if(birth_year > current_year || birth_year || current_year <= 0){
	    std::cout<<"Please enter a valid birth date.\n";
	    return 1;

	}
	    

	if(birth_year < current_year){

	     
	    age = current_year - birth_year;
	    std::cout <<"you are " <<age<< " year old.\n";

	
	}   
	
	}




