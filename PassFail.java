import java.util.Scanner;

public class PassFail {

    public static void main(String [] args) {

        Scanner scanner = new Scanner(System.in);
        
        int passCount = 0;
        int failCount = 0;

        for (int i = 1; i <= 15; i++) {
            System.out.print("Enter score for student " + i + ": ");
            int score = scanner.nextInt();

            if (score >= 45) {
               passCount++;
                }
            else {
               failCount++;
                }
              }
        System.out.println("Number of students who passed: " + passCount);
        System.out.println("Number of students who failed: " + failCount);

             }
           }