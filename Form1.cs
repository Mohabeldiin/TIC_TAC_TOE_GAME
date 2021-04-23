using System;
using System.Windows.Forms;
namespace TIC_TAC_TOE_CPP_GAME_CREATED_BY_MOHAB_MOHSEN
{
    public partial class Form1 : Form
    {
        private int Score1 = 0, Score2 = 0;
        private bool GameEnded = false;
        private enum GameStates : int
        {
            over = 1,
            progress = -1,
            no_win = 0
        } int GameState =  (int)GameStates.progress;
        private enum Players : int
        {
            one = 1,
            two = 2
        } int Player = (int)Players.one,PlayerNext;
        private GameStates CheckWin()
        {
            if (button1.Text == button2.Text && button2.Text == button3.Text && button1.Text!="") return GameStates.over;
            else if (button4.Text == button5.Text && button5.Text == button6.Text && button4.Text != "") return GameStates.over;
            else if (button7.Text == button8.Text && button8.Text == button9.Text && button7.Text != "") return GameStates.over;
            else if (button1.Text == button4.Text && button4.Text == button7.Text && button1.Text != "") return GameStates.over;
            else if (button2.Text == button5.Text && button5.Text == button8.Text && button2.Text != "") return GameStates.over;
            else if (button3.Text == button6.Text && button6.Text == button9.Text && button3.Text != "") return GameStates.over;
            else if (button1.Text == button5.Text && button5.Text == button9.Text && button1.Text != "") return GameStates.over;
            else if (button3.Text == button5.Text && button5.Text == button7.Text && button3.Text != "") return GameStates.over;
            else if (button1.Text != "" && button2.Text != "" && button3.Text != ""
                && button4.Text != "" && button5.Text != "" && button6.Text != ""
                && button7.Text != "" && button8.Text != "" && button9.Text != "") return GameStates.no_win;
            else return GameStates.progress;
        }
        private void Process(Button temp )
        {
            if (temp.AccessibleName!="Used" && !GameEnded)
            {
                Player = (int)(Player.Equals((int)Players.two) ? (int)Players.one : (int)Players.two);
                temp.Text = (Player.Equals((int)Players.two)) ? "X" : "O";
                GameState = (int)CheckWin();
                if (GameState.Equals((int)GameStates.no_win)) label1.Text = "Game State: No Win";
                else if (GameState.Equals((int)GameStates.over))
                {
                    if (Player.Equals((int)Players.two)) Score1++;
                    else Score2++;
                    label1.Text = (Player.Equals((int)Players.two)) ? "Game State: Player One Win" : "Game State: Player Two Win"; 
                    label2.Text = (Player.Equals((int)Players.two)) ? "Player One Score: " + Score1.ToString() : label2.Text;
                    label3.Text = (Player.Equals((int)Players.one)) ? "Player two Score: " + Score2.ToString() : label3.Text;
                    GameEnded = true;
                    PlayerNext = (int)Player;
                }
                else label1.Text = (Player.Equals((int)Players.two)) ? "Game State: Player One Turn" : "Game State: Player Two Turn";
                temp.AccessibleName = "Used";
            }
        }
        private void Reset()
        {
            GameEnded = false;
            button1.Text = "";
            button1.AccessibleName = "";
            button2.Text = "";
            button2.AccessibleName = "";
            button3.Text = "";
            button3.AccessibleName = "";
            button4.Text = "";
            button4.AccessibleName = "";
            button5.Text = "";
            button5.AccessibleName = "";
            button6.Text = "";
            button6.AccessibleName = "";
            button7.Text = "";
            button7.AccessibleName = "";
            button8.Text = "";
            button8.AccessibleName = "";
            button9.Text = "";
            button9.AccessibleName = "";
            Player = (int)(PlayerNext.Equals((int)Players.two) ? (int)Players.one : (int)Players.two);
            label1.Text = (Player.Equals((int)Players.one)) ? "Game State: Player One Turn" : "Game State: Player Two Turn";
        }
        public Form1() => InitializeComponent();
        private void Form1_Load(object sender, EventArgs e) { }
        private void buttonReset_Click(object sender, EventArgs e) => Reset();
        private void button1_Click(object sender, EventArgs e) => Process(button1);
        private void button2_Click(object sender, EventArgs e) => Process(button2);
        private void button3_Click(object sender, EventArgs e) => Process(button3);
        private void button4_Click(object sender, EventArgs e) => Process(button4);
        private void button5_Click(object sender, EventArgs e) => Process(button5);
        private void button6_Click(object sender, EventArgs e) => Process(button6);
        private void button7_Click(object sender, EventArgs e) => Process(button7);
        private void button8_Click(object sender, EventArgs e) => Process(button8);
        private void button9_Click(object sender, EventArgs e) => Process(button9);
    }
}