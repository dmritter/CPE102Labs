public class SimpleLoop
{
   public static int sum(int low, int high)
   {
      int low_temp = low;
      int sum = 0;
      while(high >= low_temp)
      {
         sum += low_temp;
         low_temp++;
      }
      return sum;
      
      /* TO DO:  Return the sum of the integers between
         low and high (inclusive).  Yes, this can be
         done without a loop, but the point is to
         practice the syntax for a loop.
      */
   }
}
