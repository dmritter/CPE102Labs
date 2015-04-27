import java.util.List;
import java.util.LinkedList;

public class SimpleList
{
   public static List<Integer> squareAll(List<Integer> values)
   {
      List<Integer> newValues = new LinkedList<Integer>();
      for(int i=0; i < values.size();i++)
      {
         newValues.add(values.get(i)*values.get(i));
      }
      /* TO DO: The output list, newValues, should hold as
         its elements the square of the corresponding element
         in the input list.

         Write a loop to add the square of each element from the
         input list into the output list.  Use a "foreach".
      */

      return newValues;
   }
}