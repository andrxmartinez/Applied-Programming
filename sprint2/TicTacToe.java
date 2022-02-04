package sprint2;

public class TicTacToe{
  
      private int [][]Position;
    
    // This is the constructor for the TicTacToe class. 
      public TicTacToe(){
      
        Position = new int [3][3];
      }
    //This method assigns one of the two players from the game
      public int AssignPlayer(int i, int j, int Player){
  
          if(i>=0 && i<3 && j>=0 && j < 3){
  
              if(Player==1 || Player==2){
  
                  if(Position[i][j]==0){
                      
                    Position[i][j]=Player;
                        return 1;
                  }else{
                      System.out.println("Unable to use this position, please try another one");
                  }
  
              }else{
                   System.out.println("Players 1 and 2");
              }
  
          }else{
              System.out.println("Number is way too big. Please choose one from 1-3."); 
          }
          return 0;
     }
     
     //This method determines the winner of the game based on certain conditions.
      public int Winner(){
          int i, j=0;
          for(i=0; i<3; i++) {
			for(j=1; j<3; j++) {
				if(Position[i][0]==j && Position[i][1]==j && Position[i][2]==j)return j;
   			}
   		}
   		for(i=0; i<3; i++) {
   			for(j=1; j<3; j++) {
    			if(Position[0][i]==j && Position[1][i]==j && Position[2][i]==j)return j;
   			}
   		}
   		for(i=0; i<3; i++) {
   			for(j=1; j<3; j++) {
   				if(Position[0][0]==j && Position[1][1]==j && Position[2][2]==j)return j;
   			}
   		}
   		for(i=0; i<3; i++) {
   			for(j=1; j<3; j++) {
   				if(Position[2][0]==j && Position[1][1]==j && Position[0][2]==j)return j;
   			}
   		}
		return 0;
   }
    // This method Displays the board to the screen.
	public void DisplayBoard(){
    	System.out.println(Position[0][0]+"|"+Position[0][1]+"|"+Position[0][2]);
    	System.out.println("_____");
    	System.out.println(Position[1][0]+"|"+Position[1][1]+"|"+Position[1][2]);
    	System.out.println("_____");
    	System.out.println(Position[2][0]+"|"+Position[2][1]+"|"+Position[2][2]);
	}
}