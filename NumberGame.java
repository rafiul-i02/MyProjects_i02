import java.util.Scanner;

public class NumberGame {
    
    public static void main(String[] args) {

        Scanner input = new Scanner(System.in);
        
        System.out.println("Press 'p' to play.....\n");
        String gamePlay=input.next();
        
        int gameNum = (int)(Math.random()*100)/*Random number from system.*/ , userNum=-1; /*Initialising user input.*/
        int attempt=0;

        if(gamePlay.equalsIgnoreCase("p")) {
            do{ //Using do while loop to perform the action again & again.
    
                System.out.println("Enter any positive number between 0-100 :(Press '111' to Quit the Game.)\n");
                userNum = input.nextInt(); //Taking user input number between 0-100.
    
                if (userNum==111) {
                    break; //As '111' is key to Quit the game So we're breaking the loop here.
                }

                attempt++; //Game Attempts counting.

                if (userNum>gameNum && userNum<=100) { 
                    System.out.println("Wrong Guess!! (Your number is too High)\nPlease try again.....\n"); //Indicating if the user number is higher than random number from the system.
                }
                else if (userNum<0) {
                    System.out.println("You've Entered a Negative Number!\nPlease Enter a number between 0-100!!\n"); //Disallowing Neg1tive number.
                }
                else if (userNum<gameNum &&  userNum>=0) {
                    System.out.println("Wrong Guess!! (Your number is too Low)\nPlease try again.....\n"); //Indicating if the user number is lower than random number from the system.
                }  
                else if(userNum>100){
                    System.out.println("Please Enter a number between 0-100!!\n");
                }  
                
            }while(userNum!=gameNum); //Running the loop till user number & random number are not being same.

        if(userNum==gameNum) { //Game winning condition.
            System.out.println("Congratulations!! You got the right guess :)");
            System.out.println("Total attempts = "+attempt); //printing total user attempts to the game.
            System.out.println("(Game Number was = "+gameNum+")\nGame Finished.\n"); //Showing game number.
        }
        else{
            System.out.println("Better luck next time ;)"); //Game quit.
            System.out.println("(Game Number was = "+gameNum+")\nYou've Quit the Game.\n");
        }
        }
        else{
            System.out.println("Game Quit\nYou didn't start the Game.");
        }

        input.close(); //Closing input.
    }
}
