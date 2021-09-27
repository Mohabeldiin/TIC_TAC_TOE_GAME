#include <iostream>
#include <cstdlib>
using namespace std;
enum GameStates { Over =1, Progressing=-1, NoWin=0 };
int GameState = Progressing;
enum Players { One =1, Two=2 };
int Player = One;
char Square[10] = { 'o','1','2','3','4','5','6','7','8','9' };
static char DefaultSquare[10] = { 'o','1','2','3','4','5','6','7','8','9' };
int Choice;
char Mark;
int CheckWin(int);
void Board();
void MakeMove(int);

int main()
{
	system("color f0");
	do
	{
		Board();
		Player = (Player % 2) ? One : Two ;
		Mark = (Player == One) ? 'X' : 'O';
		cout << "Player " << Player << ", Enter a Number:  ";
		cin >> Choice;
        MakeMove(Choice);
		Player++;
	} while (GameState == Progressing);
	Board();
	if (GameState == Over) cout << "==>\aPlayer " << --Player << " win ";
	else cout << "==>\aGame draw";
	cin.ignore();
	return 0;
}

/**********************************
	FUNCTION TO RETURN GAME STATUS
	1 FOR GAME IS Over WITH RESULT
	-1 FOR GAME IS IN Progressing
	O GAME IS Over AND NO RESULT
***********************************/

int CheckWin(int GameState)
{ 
	if (equal(begin(Square),end(Square),begin(DefaultSquare))) return NoWin;
	else if (Square[1] == Square[2] && Square[2] == Square[3]) return Over;
	else if (Square[4] == Square[5] && Square[5] == Square[6]) return Over;
	else if (Square[7] == Square[8] && Square[8] == Square[9]) return Over;
	else if (Square[1] == Square[4] && Square[4] == Square[7]) return Over;
	else if (Square[2] == Square[5] && Square[5] == Square[8]) return Over;
	else if (Square[3] == Square[6] && Square[6] == Square[9]) return Over;
	else if (Square[1] == Square[5] && Square[5] == Square[9]) return Over;
	else if (Square[3] == Square[5] && Square[5] == Square[7]) return Over;
	else return Progressing;
}

/**********************************************
	 FUNCTION TO Make a Move WITH Players Mark
**********************************************/

void MakeMove(int Choice)
{
    for (int Position = 1; Position <= 9;Position++) 
    {
        if (Choice == Position )
        {
            if( Square[Position] == DefaultSquare[Position]) 
            {
                Square[Position] = Mark;
                GameState = CheckWin(GameState);
                break;
            }
            else
            {
                cout << "Invalid move ";
                cin.get();
            }
        }
    }
}

/************************************************************
	 FUNCTION TO DRAW Board OF TIC TAC TOE WITH Players Mark
************************************************************/

void Board()
{
	system("cls");
	cout << "\n\n\tTic Tac Toe\n\n";
	cout << "Player 1 (X)  -  Player 2 (O)" << endl << endl << endl;
	cout << "     |     |     " << endl;
	cout << "  " << Square[1] << "  |  " << Square[2] << "  |  " << Square[3] << endl;
	cout << "_____|_____|_____" << endl;
	cout << "     |     |     " << endl;
	cout << "  " << Square[4] << "  |  " << Square[5] << "  |  " << Square[6] << endl;
	cout << "_____|_____|_____" << endl;
	cout << "     |     |     " << endl;
	cout << "  " << Square[7] << "  |  " << Square[8] << "  |  " << Square[9] << endl;
	cout << "     |     |     " << endl << endl;
}