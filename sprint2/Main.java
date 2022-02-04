package sprint2;
import java.util.Scanner;

class Main{
	public static void main(String[] args){
		TicTacToe g = new TicTacToe();

		int Player=1;
		int i ;
		int j; 
		int l;
		int winner;

		System.out.println(" |T| |I| |C|   |T| |A| |C|   |T| |O| |E|");
 		System.out.println("This is a Two Player Game, so go find a partner!");
 		System.out.println("Choose a value between 1-3 for both, rows and columns.");
  		System.out.println();
   		
		g.DisplayBoard();

		for(l=0;l<9; l++) {
		    do{
                    Scanner sc = new Scanner(System.in); 

			System.out.println("Choose a row position between 1-3:");
			i = sc.nextInt(); //This reads an integer number from 1-3

        	    System.out.println("Choose a column position between 1-3:");
           	        j = sc.nextInt(); //This reads an integer number from 1-3

			}while(g.AssignPlayer(i-1,j-1,Player)==0);
 
  			g.DisplayBoard();
			winner=g.Winner();

			if(winner==1) {
				System.out.println("We've got a winner! Player #1: You rock!");
			}
			if(winner==2) { 
				System.out.println("Congrats, Player # 2. You're a champ!");
			}
    		Player++; 
			if(Player>2) Player=1;
		}

		if (l==9){
			System.out.println("\n We're even. ");
			System.out.println("|G| |A| |M| |E|   |O| |V| |E| |R|");
		}
    }
}