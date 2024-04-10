import java.util.Scanner;

public class RightTriangle {

    public static void main(String [] args) {

        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter a number of rows for the right triangle: ");
        int num = scanner.nextInt();

        for (int i = 1; i <= num; i++) {
            for (int j = 1; j <= i; j++) {
                System.out.print("*");
                       }
            System.out.println();
               }

             }
           }