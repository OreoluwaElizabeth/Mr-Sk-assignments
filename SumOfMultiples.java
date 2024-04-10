public class SumOfMultiples{

   public static void main(String [] args) {

       int sum = 0;

       for (int num = 1; num <= 20000; num++) {
            if (num % 10 == 0) {
               sum += num;
                 }
              }
       System.out.println("The sum of multiples of 10 between 1 and 20,000 is : " + sum);
               }
             }











