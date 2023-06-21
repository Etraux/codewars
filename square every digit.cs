using System;

public class Kata
{
  public static int SquareDigits(int n)
  {
    string result = "";
    string numberString = n.ToString();
    
    foreach (char digitChar in numberString)
    {
      int digit = int.Parse(digitChar.ToString());
      int squaredDigit = digit * digit;
      result += squaredDigit.ToString();
    }
    return int.Parse(result);
  }
}