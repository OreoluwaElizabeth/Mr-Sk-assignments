import java.util.Scanner;

public class MultiplicationTable {

    public static void main(String [] args) {

        Scanner scanner = new Scanner(System.in);

       System.out.print("Enter a number: ");
       int num = scanner.nextInt();

       for (int i = 1; i <= 12; i++) {
           int result = num * i;
           System.out.println(num + " * " + i + " = " + result);
              }

            }
          }