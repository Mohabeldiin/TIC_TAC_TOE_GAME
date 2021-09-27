#include "pch.h"
#include <iostream>
#include <cstdlib>
using namespace std;
enum i
{
	over =1,
	progress=-1,
	no_win=0

};
enum player
{
	one =1,
	two=2

};
char square[10] = { 'o','1','2','3','4','5','6','7','8','9' };
int checkwin(int);
int i = progress;
void board();

int main()
{
	system("color f0");
	
	int player = one ,  choice;
	char a[10] = { 'o','1','2','3','4','5','6','7','8','9' };
	char mark;
	do
	{
		board();
		player = (player % 2) ? one : two ;
		mark = (player == one) ? 'X' : 'O';
		cout << "Player " << player << ", enter a number:  ";
		cin >> choice;

		for (int p = 1; p <= 9;p++) {
			
			if (choice == p && square[p] == a[p]) {
				
				square[p] = mark;
				i = checkwin(i);
				break;
			}
			else
				if(!(choice == p && square[p] == a[p]))
			{
					continue;
			}
				else{
					cout << "Invalid move ";
					cin.get();
				}
		}
		
		player++;
	} while (i == progress);
	board();
	if (i == over)

		cout << "==>\aPlayer " << --player << " win ";
	else
		cout << "==>\aGame draw";

	cin.ignore();
	return 0;
}

/*********************************************
	FUNCTION TO RETURN GAME STATUS
	1 FOR GAME IS OVER WITH RESULT
	-1 FOR GAME IS IN PROGRESS
	O GAME IS OVER AND NO RESULT
**********************************************/

int checkwin(int i)
{
	if (square[1] == square[2] && square[2] == square[3])

		return over;
	else if (square[4] == square[5] && square[5] == square[6])

		return over;
	else if (square[7] == square[8] && square[8] == square[9])

		return over;
	else if (square[1] == square[4] && square[4] == square[7])

		return over;
	else if (square[2] == square[5] && square[5] == square[8])

		return over;
	else if (square[3] == square[6] && square[6] == square[9])

		return over;
	else if (square[1] == square[5] && square[5] == square[9])

		return over;
	else if (square[3] == square[5] && square[5] == square[7])

		return over;
	else if (square[1] != '1' && square[2] != '2' && square[3] != '3'
		&& square[4] != '4' && square[5] != '5' && square[6] != '6'
		&& square[7] != '7' && square[8] != '8' && square[9] != '9')

		return no_win ;
	else
		return progress;
}


/*******************************************************************
	 FUNCTION TO DRAW BOARD OF TIC TAC TOE WITH PLAYERS MARK
********************************************************************/


void board()
{
	system("cls");
	cout << "\n\n\tTic Tac Toe\n\n";

	cout << "Player 1 (X)  -  Player 2 (O)" << endl << endl;
	cout << endl;

	cout << "     |     |     " << endl;
	cout << "  " << square[1] << "  |  " << square[2] << "  |  " << square[3] << endl;

	cout << "_____|_____|_____" << endl;
	cout << "     |     |     " << endl;

	cout << "  " << square[4] << "  |  " << square[5] << "  |  " << square[6] << endl;

	cout << "_____|_____|_____" << endl;
	cout << "     |     |     " << endl;

	cout << "  " << square[7] << "  |  " << square[8] << "  |  " << square[9] << endl;

	cout << "     |     |     " << endl << endl;
}

/*******************************************************************
				END OF PROJECT
********************************************************************/

