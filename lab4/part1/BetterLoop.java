public class BetterLoop
{
   public static boolean contains(int [] values, int v)
   {
      boolean check = false;
      for(int i = 0; i < values.length; i++)
      {
         if(values[i] == v)
         {
            check = true;
         }
      /* TO DO: if value v is in the array, return true.
         If not, return false.  Use a "foreach" loop.
      */
      }
      return check;  // A bit optimistic, but a real boolean value.
   }
}
